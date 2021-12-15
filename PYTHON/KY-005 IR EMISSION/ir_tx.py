# MIT License
# 
# Copyright (c) 2020 Peter Hinch
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Author: Peter Hinch
# Copyright Peter Hinch 2020-2021 Released under the MIT license
# http://github.com/peterhinch/micropython_ir

# __init__.py Nonblocking IR blaster
# Runs on Pyboard D or Pyboard 1.x (not Pyboard Lite), ESP32 and RP2

# Released under the MIT License (MIT). See LICENSE.

# Copyright (c) 2020-2021 Peter Hinch
from sys import platform
from micropython import const
ESP32 = platform == 'esp32'  # Loboris not supported owing to RMT
RP2 = platform == 'rp2'
if ESP32:
    from machine import Pin, PWM
    from esp32 import RMT
elif RP2:
    from .rp2_rmt import RP2_RMT
else:
    from pyb import Pin, Timer  # Pyboard does not support machine.PWM
from esp32 import RMT
from array import array
from time import ticks_us
from time import ticks_diff
# import micropython
# micropython.alloc_emergency_exception_buf(100)


# Shared by NEC
STOP = const(0)  # End of data

# IR abstract base class. Array holds periods in μs between toggling 36/38KHz
# carrier on or off. Physical transmission occurs in an ISR context controlled
# by timer 2 and timer 5. See TRANSMITTER.md for details of operation.
class IR:
    _active_high = True  # Hardware turns IRLED on if pin goes high.
    _space = 0  # Duty ratio that causes IRLED to be off
    timeit = False  # Print timing info

    @classmethod
    def active_low(cls):
        if ESP32:
            raise ValueError('Cannot set active low on ESP32')
        cls._active_high = False
        cls._space = 100

    def __init__(self, pin, cfreq, asize, duty, verbose):
        if ESP32:
            self._rmt = RMT(0, pin=pin, clock_div=80, carrier_freq=cfreq,
                            carrier_duty_percent=duty)  # 1μs resolution
        elif RP2:  # PIO-based RMT-like device
            self._rmt = RP2_RMT(pin_pulse=None, carrier=(pin, cfreq, duty))  # 1μs resolution
        else:  # Pyboard
            if not IR._active_high:
                duty = 100 - duty
            tim = Timer(2, freq=cfreq)  # Timer 2/pin produces 36/38/40KHz carrier
            self._ch = tim.channel(1, Timer.PWM, pin=pin)
            self._ch.pulse_width_percent(self._space)  # Turn off IR LED
            # Pyboard: 0 <= pulse_width_percent <= 100
            self._duty = duty
            self._tim = Timer(5)  # Timer 5 controls carrier on/off times
        self._tcb = self._cb  # Pre-allocate
        self._arr = array('H', 0 for _ in range(asize))  # on/off times (μs)
        self._mva = memoryview(self._arr)
        # Subclass interface
        self.verbose = verbose
        self.carrier = False  # Notional carrier state while encoding biphase
        self.aptr = 0  # Index into array

    def _cb(self, t):  # T5 callback, generate a carrier mark or space
        t.deinit()
        p = self.aptr
        v = self._arr[p]
        if v == STOP:
            self._ch.pulse_width_percent(self._space)  # Turn off IR LED.
            return
        self._ch.pulse_width_percent(self._space if p & 1 else self._duty)
        self._tim.init(prescaler=84, period=v, callback=self._tcb)
        self.aptr += 1

    # Public interface
    # Before populating array, zero pointer, set notional carrier state (off).
    def transmit(self, addr, data, toggle=0, validate=False):  # NEC: toggle is unused
        t = ticks_us()
        if validate:
            if addr > self.valid[0] or addr < 0:
                raise ValueError('Address out of range', addr)
            if data > self.valid[1] or data < 0:
                raise ValueError('Data out of range', data)
            if toggle > self.valid[2] or toggle < 0:
                raise ValueError('Toggle out of range', toggle)
        self.aptr = 0  # Inital conditions for tx: index into array
        self.carrier = False
        self.tx(addr, data, toggle)  # Subclass populates ._arr
        self.trigger()  # Initiate transmission
        if self.timeit:
            dt = ticks_diff(ticks_us(), t)
            print('Time = {}μs'.format(dt))

    # Subclass interface
    def trigger(self):  # Used by NEC to initiate a repeat frame
        if ESP32:
            self._rmt.write_pulses(tuple(self._mva[0 : self.aptr]), start = 1)
        elif RP2:
            self.append(STOP)
            self._rmt.send(self._arr)
        else:
            self.append(STOP)
            self.aptr = 0  # Reset pointer
            self._cb(self._tim)  # Initiate physical transmission.

    def append(self, *times):  # Append one or more time peiods to ._arr
        for t in times:
            self._arr[self.aptr] = t
            self.aptr += 1
            self.carrier = not self.carrier  # Keep track of carrier state
            self.verbose and print('append', t, 'carrier', self.carrier)

    def add(self, t):  # Increase last time value (for biphase)
        assert t > 0
        self.verbose and print('add', t)
        # .carrier unaffected
        self._arr[self.aptr - 1] += t


# Given an iterable (e.g. list or tuple) of times, emit it as an IR stream.
class Player(IR):

    def __init__(self, pin, freq=38000, verbose=False):  # NEC specifies 38KHz
        super().__init__(pin, freq, 68, 33, verbose)  # Measured duty ratio 33%

    def play(self, lst):
        for x, t in enumerate(lst):
            self._arr[x] = t
        self.aptr = x + 1
        self.trigger()


_TBURST = const(563)
_T_ONE = const(1687)

class NEC(IR):
    valid = (0xffff, 0xff, 0)  # Max addr, data, toggle

    def __init__(self, pin, freq=38000, verbose=False):  # NEC specifies 38KHz
        super().__init__(pin, freq, 68, 33, verbose)  # Measured duty ratio 33%

    def _bit(self, b):
        self.append(_TBURST, _T_ONE if b else _TBURST)

    def tx(self, addr, data, _):  # Ignore toggle
        self.append(9000, 4500)
        if addr < 256:  # Short address: append complement
            addr |= ((addr ^ 0xff) << 8)
        for _ in range(16):
            self._bit(addr & 1)
            addr >>= 1
        data |= ((data ^ 0xff) << 8)
        for _ in range(16):
            self._bit(data & 1)
            data >>= 1
        self.append(_TBURST)

    def repeat(self):
        self.aptr = 0
        self.append(9000, 2250, _TBURST)
        self.trigger()  # Initiate physical transmission.
