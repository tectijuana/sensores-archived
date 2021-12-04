from machine import Pin
import time

Signal_Pin = Pin(20, Pin.IN)
LED_Pin = Pin(21, Pin.OUT)

while True:
    print(Signal_Pin.value())
    LED_Pin.value(Signal_Pin.value())
    time.sleep(0.05)
