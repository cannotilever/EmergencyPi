import os
import time
import psutil
import cmd
import win32gui, win32con
import math
parentCrashCounter = 0
os.system("@echo OFF")
def OnStartup():
    print("  ---------------------------------------------")
    print("| Welcome to the HVRHS Emergency Alert System. |")
    print("  ---------------------------------------------")
    print("")
    userInput = input("Would you like to enable the alert service on your computer for this session? (Y/N): ")
    if (userInput == "Y") or (userInput == "y"):
        print("")
        print("The Emergency Alert System Endpoint is now active! This window will hide itself automatically in 5 seconds...")
        Minimize = win32gui.GetForegroundWindow()
        time.sleep(5)
        win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)
    else:
        if (userInput == "N") or (userInput == "n"):
            print("")
            print("The Emergency Alert System Endpoint is now deactivated for the duration of this session. Terminating in 5 seconds...")
            time.sleep(5)
            exit()
        print("")
        print("INVALID INPUT DETECTED. Please type Y or N!")
        print("")
        OnStartup()

OnStartup()
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
