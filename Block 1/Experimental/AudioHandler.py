import time
import os
from lxml import html
import requests

page = requests.get('http://192.168.86.131/generalAlarm.html')
tree = html.fromstring(page.content)
status = tree.xpath('//h1/text()')
while status == ['Emergency']:
	global page, tree, status
	os.system('mpg321 /home/pi/Music/Siren1.mp3')
	page = requests.get('http://192.168.86.131/generalAlarm.html')
	tree = html.fromstring(page.content)
	status = tree.xpath('//h1/text()')
	if(status != ['Emergency']):
		break
	time.sleep(19)
print "exited Audio Handler at", time.time()
