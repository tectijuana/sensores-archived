import RPi.GPIO as GPIO
import time


KY002 = 7
LED = 11


def toggle_led(null):  # Función para activar LED on/off cuando detecte una señal
    if GPIO.input(LED):
        GPIO.output(LED, GPIO.LOW)  # Si el LED está encendido, se apaga
    else:
        GPIO.output(LED, GPIO.HIGH)  # Si el LED está apagado, se enciende


GPIO.setmode(GPIO.BOARD)
GPIO.setup(KY002, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED, GPIO.OUT)

# Cuando una vibración es detectada, la función toggle_led será activada.
GPIO.add_event_detect(KY002, GPIO.FALLING, callback=toggle_led, bouncetime=100)

print("Use CTRL+C to exit.")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
