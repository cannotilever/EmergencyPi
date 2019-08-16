import os
import time
import psutil
parentCrashCounter = 0
while True:
    time.sleep(3)
    if ("py.exe" in (p.name() for p in psutil.process_iter())):
        print ("All is well")
    else:
        print ("Parent is Down!!! relaunching...")
        os.system("py.exe C:\\Program Files\\EmergencyAlertEndpoint\\WorkstationEndpoint.py")
        parentCrashCounter += 1
        if parentCrashCounter == 4:
            os.system("py.exe C:\\Program Files\\EmergencyAlertEndpoint\\MessageSpawn.py")
