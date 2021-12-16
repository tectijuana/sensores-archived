#INICIO DEL EJEMPLO PARA UN RELEVADOR EN RASPBERRY PI PICO

#Revisado por: Daniel Garcia - 18212185
#NOTA: No tendras un codigo que no use la libreria de RPi? no es soportada por la Pico

import RPi.GPIO as GPIO     # import GPIO librarie
  
GPIO.setmode(GPIO.BCM)
  
GPRelayPIN = 21
GPIO.setup(GPRelayPIN, GPIO.OUT)
GPIO.output(GPRelayPIN, False)
  
while True:
    # activate the relay
    # normally closed pin stops sending current
    # normally open pin starts sending current
    GPIO.output(GPRelayPIN, True) 
    time.sleep(2) #sleep 2 seconds
     
    # deactive the relay
    # normally closed pin starts sending current
    # normally open pin stops sending current
    GPIO.output(GPRelayPIN, False) # NC is now connected through
    time.sleep(2)
    
    #brychxpin was here
