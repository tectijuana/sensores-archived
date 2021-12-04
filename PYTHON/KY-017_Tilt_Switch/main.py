# Required modules are imported and set up
# import RPi.GPIO as GPIO
from machine import Pin
import time
   
# GPIO.setmode(GPIO.BCM)
   
a = Pin(24, Pin.IN)

# GPIO.setup(GPIO_PIN, GPIO.IN)
   
# This outputFunction will be executed on signal detection
def outputFunction(null):
        print("Signal detected")
   
# When a signal is detected (falling signal edge) the output function is executed
GPIO.add_event_detect(a, GPIO.FALLING, callback=outputFunction, bouncetime=100) 
   
# main program loop
try:
    while True:
        time.sleep(1)
   
# clean up after the program is finished
except KeyboardInterrupt:
    GPIO.cleanup()
