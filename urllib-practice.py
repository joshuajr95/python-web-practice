
# for python 2, use urllib, but for python 3 use urllib.request, urllib.parse, urllib.error

import urllib.request, urllib.parse, urllib.error


fhand = urllib.request.urlopen('http://www.google.com')
#charset = fhand.info().get_charset()
#print(charset)


for line in fhand:
	line = line.decode(encoding='latin1').strip()
	text1 = line.split("<")
	print(text1)


