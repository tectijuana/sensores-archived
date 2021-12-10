#Amador Garcia Fernando

#Revisado por Daniel García Chacón - 18212185
#NOTA: La RPI Pico no soporta la libería RPi, solo es para la RPI 3


import RPi.GPIO as GPIO
from time import sleep
 
counter = 10
 
Enc_A = 17  
Enc_B = 27  
 
 
def init():
    print "Rotary Encoder Test Program"
    GPIO.setwarnings(True)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Enc_A, GPIO.IN)
    GPIO.setup(Enc_B, GPIO.IN)
    GPIO.add_event_detect(Enc_A, GPIO.RISING, callback=rotation_decode, bouncetime=10)
    return
 
  
  def rotation_decode(Enc_A):
    global counter
    sleep(0.002)
    Switch_A = GPIO.input(Enc_A)
    Switch_B = GPIO.input(Enc_B)
 
    if (Switch_A == 1) and (Switch_B == 0):
        counter += 1
        print "direction -> ", counter
        while Switch_B == 0:
            Switch_B = GPIO.input(Enc_B)
        while Switch_B == 1:
            Switch_B = GPIO.input(Enc_B)
        return
 
    elif (Switch_A == 1) and (Switch_B == 1):
        counter -= 1
        print "direction <- ", counter
        while Switch_A == 1:
            Switch_A = GPIO.input(Enc_A)
        return
    else:
        return
 
def main():
    try:
        init()
        while True :
            sleep(1)
 
    except KeyboardInterrupt:
        GPIO.cleanup()
 
if __name__ == '__main__':
    main()
