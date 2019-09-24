# This program is NOT production software. It initializes the Raspberry Pi's GPIO pins and prints wheather or not a button press is registered
import time
import RPi.GPIO as GPIO
GPIO.cleanup()
time.sleep(0.1)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(24, GPIO.IN)
print GPIO.RPI_INFO
while True:
	print GPIO.input(24)
	time.sleep(1)
print "you should never see this"
