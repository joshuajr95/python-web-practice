import urllib.request
import urllib.parse
import urllib.error
import ssl
from bs4 import BeautifulSoup


# ignore SSL certificate errors
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE


# have user enter a URL to read HTML from
url = input("Enter a URL: ")
urlHandle = urllib.request.urlopen(url, context=context)
html = urlHandle.read()

soup = BeautifulSoup(html, 'html.parser')

anchorTags = soup('a')

for tag in anchorTags:
	print(tag.get('href'))