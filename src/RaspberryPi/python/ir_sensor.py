import os 
from gpiozero import LED
from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO
import time

sensor = 18
led = LED(17) 
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
            led.on()
            camera.start_preview()
            nr = nr + 1
            nrStr = str(nr)
            fileName = […]
            […] '/media/pi/9016-4EF8/ […]
            […]  video' + nrStr + '.h264' 
            camera.start_recording(fileName)
            sleep(600)
            camera.stop_recording()
            camera.stop_preview()
            led.off()




    try:
        while True:
            if nr == 20:
             for filename in os.listdir […]
            […] ('/media/pi/9016-4EF8'): 
                 os.remove('video' + nrStr + '.h264')
                 print ("gelöscht")
                 
            else: print("ng")



except KeyboardInterrupt: 
    GPIO.cleanup()        



