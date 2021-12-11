# Los módulos necesarios serán importados y configurados

# Revisado por Aquino Villegas Daniel 18212144
# La placa que se esta usando es la raspberry pi pico
# La Libreria RPi No esta en funcionamiento, tienes que cambiarla por la libreria machine

import RPi.machine as machine
import time
  
machine.setmode(machine.BCM)
  
# El pin de entrada que está conectado con el sensor

machine_PIN = 21
machine.setup(machine_PIN, GPIO.IN, pull_up_down = machine.PUD_DOWN)
  
print "KY-010 Sensor Test [press ctrl+c to end the test]"
  
def outputFunction(null):
        print("Sensor is blocked")
  
# detección de señal (flanco ascendente).

machine.add_event_detect(machine_PIN, GPIO.RISING, callback=outputFunction, bouncetime=100) 
  
# Bucle del programa principal

try:
        while True:
                time.sleep(1)
  
# Trabajo de recolección de residuos una vez finalizado el programa

except KeyboardInterrupt:
        machine.cleanup()
