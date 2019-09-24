import pifacedigitalio as pfio
import time

pfio.init()

time.sleep(0.5)

while True:
	print "silent alarm:", (pfio.digital_read(6))
	time.sleep(0.5)
