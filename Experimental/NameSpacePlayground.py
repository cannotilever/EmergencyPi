import time
import math
global x = 11
def Void1():
	x = 10
	print ("void1x"), (x)
def Void2():
	nonlocal x
	print ("void2x"), (x)
Void1()
Void2()

