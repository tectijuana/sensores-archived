#Revisado por Daniel Garcia - 18212185
#NOTA: La libreria de RPI no es aceptada por la Pi Pico, solo por la RP3

import RPi. GPIO  as  GPIO
import time
   
GPIO.setmode (GPIO.BCM) 
   
GPIO_PIN = 24
GPIO.setup (GPIO_PIN, GPIO.IN) 
   
print ("Sensor test [press CTRL+C to exit the test]")
   

def outputFunction(null) :
    print("Signal detected")
   
GPIO.add_event_detect(GPIO_PIN, GPIO.FALLING, callback= outputFunction ,  bouncetime=100)  
   
try:
    while True:
        time.sleep (1) 
   
except KeyboardInterrupt:
    GPIO.cleanup ()
