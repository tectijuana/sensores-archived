
import rp2
rp2.country('MX')
import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.config(pm = 0xa11140)

import ubinascii
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
print(mac)

# Other things you can query
print('Channel: ',wlan.config('channel'))
print('essid', wlan.config('essid'))
print('txpower',wlan.config('txpower'))

