import rp2
from machine import Pin
from rp2 import PIO
import time

@rp2.asm_pio(out_init=[PIO.OUT_LOW])
def echo():
    wrap_target()
    mov(pins, isr)     
    mov(isr, invert(isr))
    pull(noblock)      
    mov(x, osr)
    mov(y, x)
    label("loop")
    jmp(y_dec, "loop")  
    wrap()

sm = rp2.StateMachine(0, echo, freq=1_000_000, out_base=Pin(7))
sm.active(1)

def play(freq):
  if freq:
    sm.put(1_000_000//freq)
  else:
    sm.put(0)

def looped():
  play(500)
  time.sleep(1)
  play(1000)
  time.sleep(1)
  play(0)

while True:
  looped()