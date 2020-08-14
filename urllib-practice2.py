import urllib.request
import urllib.parse
import ssl


#url = urllib.request.urlopen('http://www.google.com')

#print(url.read())

# ignore SSL certificate errors
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

url = 'http://pythonprogramming.net'

#searchQuery = input("Enter something to search on Google: ")

values = {'s':'basic', 'submit':'search'}

# urlencode encodes a sequence of key value pairs to be used
# for an HTTP POST request
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')

request = urllib.request.Request(url, data, method='POST')
response = urllib.request.urlopen(request)
responseData = response.read()

print(responseData)