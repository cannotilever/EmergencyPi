# file Hello world.py Created to learn WTF I'm doing
import random
print "!"

# file-output.py
f = open('/var/www/html/index.html','w')
f.write("<!DOCTYPE html><html lang="en">
<h1 style="text-align: center;">Emergency</h1>
<p>The HVRHS Emergency Alert Systems have triggered an emergency protocol. This may include Fire, Medical, or lockdown. DO NOT enter the building.&nbsp;</p>
</body></html>
")
f.close()
