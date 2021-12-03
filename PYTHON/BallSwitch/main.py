import RPi.GPIO as GPIO
import time
   
GPIO.setmode(GPIO.BCM)
GPIO_PIN = 27
GPIO.setup(GPIO_PIN, GPIO.IN)
   
print("Sensor-test [press ctrl+c para finalizar]")
  
def outFunction(null):
        print("Señal detectada")
   
GPIO.add_event_detect(GPIO_PIN, GPIO.FALLING, callback=outFunction, bouncetime=100) 
   
try:
        while True:
                time.sleep(1)
except KeyboardInterrupt:
        GPIO.cleanup()
