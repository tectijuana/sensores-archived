# Required modules are imported and set up
# import RPi.GPIO as GPIO
from machine import Pin
import time
   
# GPIO.setmode(GPIO.BCM)
   
a = Pin(22, Pin.IN)

# GPIO_PIN = 22
# GPIO.setup(GPIO_PIN, GPIO.IN)
   
# This outputFunction will be executed on signal detection
def outputFunction(null): 
   print("Signal detected")
   
# When a signal is detected (falling signal edge) the output function is executed
# GPIO.add_event_detect(GPIO, GPIO.FALLING, callback=outputFunction, bouncetime=100)

Pin.add_event_detect(a, Pin.IRQ_FALLING, callback=outputFunction, bouncetime=100)
   
while True:
   time.sleep(1)
