from SendMail import *

import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)


pin17 = 17

GPIO.setup(pin17, GPIO.IN)


try:

	while(True):
		print(GPIO.input(17))
		#if(GPIO.input(pin17)==1):
			#SendMail("Puerta Abierta!","vladgoia2811@gmail.com","kernelpanic1999","vladgoia2811@yahoo.com","ALARMA")
			#time.sleep(20)

		time.sleep(0.5)


except KeyboardInterrupt:
	print("Alarma Desactivada")


GPIO.cleanup()