#!/usr/bin/python
# Import modules for CGI handling
import cgi, cgitb
import os
import random
randNum = random.random()
print "Content-Type: text/html\n\n"
print "<html>"
print "<head>"
print "<title>System Online</title>"
print "</head>"
print "<body>"
print "<h1>System Online</h1>"
print "<h2>Random Number is: %s</h2>" % (randNum)
print "<p>This Random Number is generated on a page refresh, if it does not change when refreshed, the server has encountered an error.</p>"
print "</body>"
print "</html>"
