from machine import Pin
from utime import sleep
sound_sensor=Pin(28,Pin.IN)
led=Pin(15,Pin.OUT)
buzzer=Pin(16,Pin.OUT)
clap_count=1

while True:
  led.value(1)
  if sound_sensor.value()==1 and clap_count==1:
  led.value(1)
  sound_sensor.value(0)
  sleep(0.50)
  if sound_sensor.value()==1 and clap_count==2:
  buzzer.value(1)
  clap_count=3
  sound_sensor.value(0)
  sleep(0.5)
  if sound_sensor.value()==1 and clap_count==3:
  led.value(0)
  buzzer.value(0)
  clap_count=1
  sound_sensor.value(0)
  sleep(0.5)
