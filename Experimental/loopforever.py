#this code tests infinite listener loops
import time
import random
while True:
	print(random.randint(1, 25))
	time.sleep(1)
#I think the loop should stop here and the below code won't run
print "if you see this, that's bad"

