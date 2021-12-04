# Required modules are imported and set up
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Here the input pin is declared, to which the sensor is connected. Additionally the PullUP resistor at the input will be activated
GPIO_PIN = 24
GPIO.setup(GPIO_PIN, GPIO.IN)

print ("Sensor test [press CTRL+C to end test]")

# This outputFunction will be executed on signal detection
def outputFunction(null):
        print("Signal detected")

# When a signal is detected (falling signal edge) the output function is executed
GPIO.add_event_detect(GPIO_PIN, GPIO.FALLING, callback=outputFunction, bouncetime=100) 

# main program loop
try:
    while True:
        time.sleep(1)

# clean up after the program is finished
except KeyboardInterrupt:
    GPIO.cleanup()
