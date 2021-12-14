import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO_PIR = 24
print "KY-003 Module Test (CTRL-C = exit)"

GPIO.setup(GPIO_PIR, GPIO.IN, pull_up_down = GPIO.PUD_UP)
def printFunction(channel):
    print("Detected")
    GPIO.add_event_detect(GPIO_PIR, GPIO.RISING, callback=printFunction)
try:
    while True :
        Current_State = GPIO.input(GPIO_PIR)
        except KeyboardInterrupt:
GPIO.cleanup()
