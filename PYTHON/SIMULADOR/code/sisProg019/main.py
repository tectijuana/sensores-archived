import machine
import pyb
import utime

# The pyboard has four simple servo connections
servo = pyb.Servo(1)

servo.angle(90, 5000)
utime.sleep(1)
servo.angle(0, 5000)
utime.sleep(1)