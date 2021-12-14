import machine
import utime

sensor = machine.Pin(26, machine.Pin.IN) #entrada Analogica del sensor
inDigital = machine.Pin(16, machine.Pin.IN) #entrada Digital del sensor
led = machine.Pin(15, machine.Pin.OUT) #Salidad led
adcIN = machine.ADC(sensor)

while True:
    
    if inDigital.value() == 1: #leemos el valor de la entada digital y probamos si es true
        led.value(1) #Activa led
        print("1") #imprimo
    if inDigital.value() == 0:
        led.value(0)
        print("0")
    utime.sleep_ms(100)
