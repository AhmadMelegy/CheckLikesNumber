import urllib2
import time
import pyglet

def getFansNumber(page, first, last):
    try:
        start = page.index(first) + len(first)
        end = page.index(last,start)
        return page[start:end]
    except ValueError:
        print "Error Occured !"

def exiter(length):
	pyglet.app.exit()
	exit()

while(1):
	try:
		request = urllib2.Request('https://www.facebook.com/CATReloaded')
		response = urllib2.urlopen(request)
		web_page = response.read()
	except Exception:
		print "Error, Check your connection !"
		exit()

	fansNumber = getFansNumber(web_page,'<span class="_52id _50f5 _50f7">','<span')

	if(fansNumber >= '2,000'):
		print "Mission Accompilished !"
		sound = pyglet.media.load("beep.wav")
		sound.play()
		pyglet.clock.schedule_once(exiter, sound.duration)
		pyglet.app.run()

	else:
		time.sleep(60)