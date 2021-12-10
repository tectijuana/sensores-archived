# Codificado por Avila Jimenez David Alfredo
# Modificado por Alvarez Espinoza Raul

from machine import ADC
from utime import sleep
from math import log

sensor = ADC(26)
factor = 5 / 65535

while True:
    voltaje = sensor.read_u16()
    
    ohms = 10000 * (65535 / voltaje - 1.0)
    
    temp_C = (1.0 / (0.001129148 + (0.000234125 * log(ohms)) + 0.0000000875741 * log(ohms) * log(ohms))) - 273.15
    
    print('Temp: ' + str(voltaje) + ' C')
    sleep(0.5)
