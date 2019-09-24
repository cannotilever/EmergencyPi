import os
import time
import psutil
import cmd
import win32gui
import win32con
import math
import subprocess
parentCrashCounter = 0
print("  ---------------------------------------------")
print("| Welcome to the HVRHS Emergency Alert System. |")
print("  ---------------------------------------------")
print("")
print("The Emergency Alert System Endpoint is now active!")
print("This window will hide itself automatically in 2 seconds...")
Minimize = win32gui.GetForegroundWindow()
time.sleep(2)
win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)
while True:
    time.sleep(3)
    if ("py.exe" in (p.name() for p in psutil.process_iter())):
        print("All is well")
    else:
        print("Parent is Down!!! relaunching...")
        subprocess.call(['py.exe', 'C:\\Program Files\\EmergencyAlertEndpoint\\WorkstationEndpoint.py'])

        parentCrashCounter += 1
        if parentCrashCounter == 4:
            subprocess.call(['py.exe', 'C:\\Program Files\\EmergencyAlertEndpoint\\MessageSpawn.py'])
