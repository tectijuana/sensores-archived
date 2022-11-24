# Archivo de diagnostico cuando recibe una pico desauseada del Sistemas Programables 22AB

# Quitar el ahorro de energia del CHIP, full power
import rp2
rp2.country('MX')
import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.config(pm = 0xa11140)

# Preparar el templete del diagnostico
import ubinascii
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
print(mac)

# Other things you can query
print('Channel: ',wlan.config('channel'))
print('essid', wlan.config('essid'))
print('txpower',wlan.config('txpower'))

# Choose View -> Plotter in Thonny to see a graph of the results

from time import sleep
from picozero import pico_temp_sensor
# LED
from picozero import pico_led
from time import sleep

while True:
    print(pico_temp_sensor.temp)
    sleep(0.1)
    pico_led.on()
    sleep(0.5)
    pico_led.off()
    sleep(0.5)
