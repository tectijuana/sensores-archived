from machine import Pin, I2C
from time import sleep
import dht
 
sensor = dht.DHT22(Pin(2)) 
 
while True:
    sensor.measure()
    temp = str(sensor.temperature())
    hum = str(sensor.humidity())
    print("Temperature: ",end='')
    print(temp +" C",0,10)
    print("Humidity: ",end='')
    print(hum + " %",0,45)
    sleep(2)