# Codificado por Avila Jimenez David Alfredo
# Modificado por Alvarez Espinoza Raul

import machine
from utime import sleep
from math import log

def main():
    sensor_temperatura = machine.ADC(26)
    c1 = 0.001129148
    c2 = 0.000234125
    R1 = 10000
    c3 = 0.0000000876741

    while True:
        voltaje = sensor_temperatura.read_u16()
        R2 = R1 * (65535.0 / voltaje - 1.0)
        logR2 = log(R2)
        temperatura = (1.0 / (c1 + c2*logR2 + c3*logR2*logR2*logR2))
        print('Temperatura: ' + temperatura + ' °C')
        sleep(2)

if __name__ == '__main__':
    main()
