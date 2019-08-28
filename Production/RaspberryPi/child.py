import os
import time
import psutil
import math
import subprocess
parentCrashCounter = 0
PROCNAME = "python3 FinalFlasher.py"
while True:
        time.sleep(5)
        FoundParent = False
        for proc in psutil.process_iter():
                if proc.name() == PROCNAME:
                        FoundParent = True
        if FoundParent:
                print("All is well")
        else:
                print("Parent is Down!!! Relaunching...")
                #subprocess.Popen(['python3', '/home/pi/Documents/FinalFlasher.py'])
                parentCrashCounter =+ 1
                if parentCrashCounter >= 10:
                        os.system("sudo reboot now")
                os.system("python3 /home/pi/Documents/FinalFlasher.py")
