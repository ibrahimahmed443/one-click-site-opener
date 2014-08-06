import webbrowser
from time import sleep

f = open('websites.txt')
delay = float(f.readline())

for url in f.readlines():
    url = url.rstrip("\n")
    print "opening %s" % url
    webbrowser.open(url)
    sleep(delay)
