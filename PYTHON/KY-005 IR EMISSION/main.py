#KY-005 IR Emission

import machine
from ir_tx import NEC
import utime

sensorIR = machine.Pin(26, machine.Pin.OUT) #ADC0 sera mi salida de datos analogicos
sensorIR.value(0)# asignamos valor
nec = NEC(sensorIR)
sw = machine.Pin(0,machine.Pin.IN)

while True:
    if sw.value() == 0:
        nec.transmit(0x0000, 0x09) #trasfiero este valor
    machine.sleep_ms(100)
