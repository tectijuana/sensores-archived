//Revisado por Daniel Garcia - 18212185
//ACTUALIZADO ADRIANA PEREA

import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

i2c = busio.I2C(board.SCL, board.SDA)

ads = ADS.ADS1115(i2c)

chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
chan2 = AnalogIn(ads, ADS.P2)
chan3 = AnalogIn(ads, ADS.P3)

delayTime = 1
Digital_PIN = 24

GPIO.setup(Digital_PIN, GPIO.IN, pull_up_down = GPIO.PUD_OFF)

while True:
    analog = '%.2f' % chan0.voltage
 
    
    if GPIO.input(Digital_PIN) == False:
        print ("Analog voltage value:", analog, "V, ", "Limit: not yet reached")
    else:
        print ("Analog voltage value:", analog, "V, ", "Limit: reached")
    print ("---------------------------------------")

    button_pressed = False
    time.sleep(delayTime)
