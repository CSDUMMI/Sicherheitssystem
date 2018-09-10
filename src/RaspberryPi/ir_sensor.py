from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO
import time

sensor = 18
camera = PiCamera()

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor,GPIO.IN)

print  ("IR Sensor Ready.....")

nr = 0

try:
    while True:
        if  GPIO.input(sensor):
            print ("C")
            

        else:
            print("O")
            camera.start_preview()
            nr = nr + 1
            nrStr = str(nr)
            fileName = '/media/pi/INTENSO/video' + nrStr + '.h264'
            camera.start_recording(fileName)
            sleep(5)
            camera.stop_recording()
            camera.stop_preview()


except KeyboardInterrupt:
    GPIO.cleanup()


