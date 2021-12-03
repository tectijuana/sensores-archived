

import RPi.GPIO as GPIO
import time


BUZZER_PIN = 7  


def play_sound(duration, frequency):  
    for i in range(duration):
        GPIO.output(BUZZER_PIN, GPIO.HIGH)
        time.sleep(frequency)
        GPIO.output(BUZZER_PIN, GPIO.LOW)
        time.sleep(frequency)


GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

notes = {  # Contiene las escalas de frecuencia
    'C': 0.002109, 'D': 0.001879, 'E': 0.001674, 'F': 0.001580, 'G': 0.001408,
    'A': 0.001254, 'B': 0.001117, 'C1': 0.001054,
}

for n in ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C1']:  # Play all notes
    play_sound(100, notes[n])

GPIO.cleanup()  
