# Librerias
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# GPIO 24
Button_PIN = 24
GPIO.setup(Button_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)

delayTime = 0.2
# Crear el Bus I2C
i2c = busio.I2C(board.SCL, board.SDA)

# Crear el objeto ADC usando el bus I2C
ads = ADS.ADS1115(i2c)

# Crear una entrada de un solo extremo en los canales
chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
chan2 = AnalogIn(ads, ADS.P2)
chan3 = AnalogIn(ads, ADS.P3)


while True:
    # Los valores actuales se registran
    x = '%.2f' % chan0.voltage
    y = '%.2f' % chan1.voltage
