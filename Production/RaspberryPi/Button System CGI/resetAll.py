#!/usr/bin/python
import time
import os
import math
import subprocess
def DisplayWebpage():
        print "Content-Type: text/html\n\n"
        print "<html>"
        print "<head>"
        print "<title>All alarms reset!</title>"
        print "</head>"
        print "<body>"
        print "<h1>The Alarms have been reset.</h1>"
        print "</body>"
        print "</html>"

os.system("sudo cp /home/pi/Documents/WebPages/Nominal.html /var/www/html/generalAlarm.html")
os.system("sudo cp /home/pi/Documents/WebPages/Nominal.html /var/www/html/silentAlarm.html")
subprocess.Popen(['sudo', 'python3', '/home/pi/Documents/ButtonFinal.py'])
DisplayWebpage()
