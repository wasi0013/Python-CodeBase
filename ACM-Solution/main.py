import urllib2
print 'Content-Type: text/html'
url = "http://www.google.com/"
result = urllib2.urlopen(url)
print "a"
print"%s" % str(result)
