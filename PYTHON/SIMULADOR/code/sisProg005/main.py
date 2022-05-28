import rp2
from rp2 import PIO
from machine import Pin
from time import sleep

@rp2.asm_pio(set_init=[PIO.IN_HIGH]*4)
def keypad():
    wrap_target()
    set(y, 0)                             # 0
    label("1")
    mov(isr, null)                        # 1
    set(pindirs, 1)                       # 2
    in_(pins, 4)                          # 3
    set(pindirs, 2)                       # 4
    in_(pins, 4)                          # 5
    set(pindirs, 4)                       # 6
    in_(pins, 4)                          # 7
    set(pindirs, 8)                       # 8
    in_(pins, 4)                          # 9
    mov(x, isr)                           # 10
    jmp(x_not_y, "13")                    # 11
    jmp("1")                              # 12
    label("13")
    push(block)                           # 13
    irq(0)
    mov(y, x)                             # 14
    jmp("1")                              # 15
    wrap()

for i in range(10, 14):
  Pin(i, Pin.IN, Pin.PULL_DOWN)

def oninput(machine):
  keys = machine.get()
  while machine.rx_fifo():
    keys = machine.get()
  #print(keys)
  if(keys==1):
    print("*")
  if(keys==2):
    print("7")
  if(keys==4):
    print("4")
  if(keys==8):
    print("1")
  if(keys==16):
    print("0")
  if(keys==32):
    print("8")
  if(keys==64):
    print("5")
  if(keys==128):
    print("2")
  if(keys==256):
    print("#")
  if(keys==512):
    print("9")
  if(keys==1024):
    print("6")
  if(keys==2048):
    print("3")
  if(keys==4096):
    print("D")
  if(keys==4096*2):
    print("C")
  if(keys==4096*4):
    print("B")
  if(keys==4096*8):
    print("A")
    
sm = rp2.StateMachine(0, keypad, freq=2000, in_base=Pin(10, Pin.IN, Pin.PULL_DOWN), set_base=Pin(6))
sm.active(1)
sm.irq(oninput)
