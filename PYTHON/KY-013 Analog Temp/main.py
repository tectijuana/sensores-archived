import machine
from utime import sleep

def main():
    sensor_temperatura = machine.ADC(26)
    factor_16 = 3.3 / (65535)

    while True:
        voltaje = sensor_temperatura.read_u16() * factor_16
        temperatura = 27 - (voltaje - 0.706)/0.001721
        print(temperatura)
        sleep(2)

if __name__ == '__main__':
    main()
