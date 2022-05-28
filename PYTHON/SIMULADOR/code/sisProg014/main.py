from machine import ADC
from time import sleep

adc = ADC(26)

while True:
    value = adc.read_u16()
    print("Analog value is: " + str(value))
    sleep(0.25)