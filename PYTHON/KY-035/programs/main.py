

# inicio del programa del sensor mágnetico

# ! /usr/bin/python
#  coding = utf-8

import time
import board
import busio
import  adafruit_ads1x15.ads1115 as  ADS
from  adafruit_ads1x15.analog_in import AnalogIn

#  Create the I2C bus
i2c  =  busio. I2C (board. SCL, board. SDA)

#  Create the  ADC object  using the  I2C  bus
ads  =  ADS.ADS1115(i2c)
voltageMax  =  3.3
#  Create single-ended input on channels
chan0  =  AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
chan2 =  AnalogIn(ads, ADS.P2)
chan3 = AnalogIn(ads, ADS.P3)


while True:
    resistance  =  chan0.voltage / (voltageMax – chan0.voltage)   *  10 000

    print (“Voltage value: “,'%.2f'  % chan0.voltage”,V, resistance:  ",'%.2f' % resistance,  "ÃŽÂ©" )
    print("---------------------------------------------------")
    time.sleep(1)


# brychxpin was here

