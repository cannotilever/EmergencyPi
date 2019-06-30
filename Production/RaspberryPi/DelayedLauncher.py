#Because the rc.local launcher starts the Flasher program before the network is initialized, causing a boot loop, This program will be executed in it's stead, waiting 10 seconds then starting the actual script.
import os
import time
from subprocess import call

print "Delayed Launcher has been called"
time.sleep(10)
print "starting Flasher Program now!!"
os.system("sudo python /home/pi/Programming/Production/FlasherScript.py")
