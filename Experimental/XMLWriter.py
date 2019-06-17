#This is a test of the feasibility of a crash handler watchdog
import os
import time
import math
import lxml
import xml.etree.ElementTree as ET

RunCounter = 0
while True:
	global RunCounter
	RunCounter += 1
	# create the file structure
	data = ET.Element('data')  
	runcounter = ET.SubElement(data, 'runcounter')  
	runcounter.set('name','runcounter')  
	runcounter.text = RunCounter

	# create a new XML file with the results
	mydata = ET.tostring(data)  
	myfile = open("RunCounter.xml", "w")  
	myfile.write(mydata)
	print "Loop Number= ", RunCounter
	time.sleep(2)
