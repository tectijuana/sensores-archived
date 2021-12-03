
# Importar los módulos importantes - Pin, ADC y Utime
from machine import Pin, ADC
import utime

# Crea las variables x y yAxis. Luego, asignarlas a los pines GPIO. xAxis se asignará al pin 27 y yAxis se asignará al pin 26. 
xAxis = ADC (Pin (27))
yAxis = ADC (Pin (26))

#  Crea una variable de botón. Esto ayuda a alternar el joystick y a enviar señales.
button = Pin (16,Pin.IN, Pin.PULL_UP)

# Comprueba e imprime el valor de x, y y botón a través de un bucle continuo. 
while True:
    xValue = xAxis.read_u16()
    yValue = yAxis.read_u16()
    buttonValue = button.value ()
    xStatus = "middle"
    yStatus = "middle"
    buttonStatus = "not pressed"
    # etiquetar el estado del joystick y de los botones dentro del bucle mediante sentencias if/then.
    if xValue <= 600:
        xStatus = "left"
    elif xValue >= 60000:
        xStatus = "right"
    if yValue <= 600:
        yStatus = "up"
    elif yValue >= 60000:
        yStatus = "down"
    if buttonValue == 0:
        buttonStatus = "pressed"
      # por encima del comando sleep, se escribe una sentencia print para mostrar las variables. 
    print ("X: " + xStatus + ", Y: " + yStatus + " -- button " + buttonStatus)
    utime.sleep(0.1)
