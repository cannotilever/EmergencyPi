 #this is a script to move and rename files to manipulate the built-in web server for Pi-to-Pi comms
import os
import shutil
import time
#formula for copy operation. Origional: /home/pi/Programming/WebPages/ Destination: /var/www/html/
#formula for rename system: index.html

shutil.copyfile("/home/pi/Programming/WebPages/Nominal.html", "/var/www/html/index.html")
print "coppied Nominal"
time.sleep(10)
shutil.copyfile("/home/pi/Programming/WebPages/Emergency.html", "/var/www/html/index.html")
print "coppied Emergency"
print "Done!"
