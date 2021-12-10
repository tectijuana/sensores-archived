```python
# Importación de librerias, para el display OLED, la interfaz entre el I2C y Pi Pico,
# Controlar tiempos y para trabajar con el sensor, respectivamente
from pico_i2c_lcd import I2cLcd
from machine import Pin, I2C
from time import sleep
from dht import  DHT11

# Declarando que vamos a usar el Pin de nuestro RPI
pin = Pin(15)
dht11 = DHT11(pin,None,dht11=True)

#Declarando el uso de nuestra pantalla I2C OLED, incluyendo la frecuencia en bauds, y los Pins
i2c_lcd = I2C(id=1,scl=Pin(3),sda=Pin(2),freq=100000)

lcd = I2cLcd(i2c_lcd, 0x27, 2, 16)

while True:
    sleep(1)
    T,H = dht11.read() #Leyendo la temperatura y humedad
    if T is None:
        print("Conectar sensor") #Si no se detecta el sensor, tirar mensaje
    else:
        print("Temperatura :" + str(T) + "°C   "+ "Humedad:"+ str(H) +"%")
    # Este codigo es para imprimir en la pantalla
    lcd.move_to(0,0)
    lcd.putstr("Temperatura: " + str(T) + chr (0xDF) + "C")
    lcd.move_to(0,1)
    lcd.putstr("Humedad: "+ str(H) +"%")
    sleep(0.5)     
```
