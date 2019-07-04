from lxml import html
import requests

page = requests.get('http://192.168.86.114/index.html')
tree = html.fromstring(page.content)

SystemState = tree.xpath('//h1/text()')

print "System Status", SystemState
