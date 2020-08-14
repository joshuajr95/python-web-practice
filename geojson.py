import urllib.request
import urllib.parse
import urllib.error
import json


# this is the url for the Google Maps geocoding API
googleMapsURL = 'https://maps.googleapis.com/maps/api/geocode/json?'

print('To use this program, enter an address as either a full address, or a city, state format.')

while True:
	address = input('Enter location: ')

	if len(address) < 1:
		break

	# encode the URL properly so the API will understand the request
	url = googleMapsURL + urllib.parse.urlencode({'address' : address})

	print('Retrieving', url)
	urlHandle = urllib.request.urlopen(url)
	urlData = urlHandle.read().decode()
	print('Retrieved', len(data), 'characters')

	try:
		js = json.loads(data)

	except Exception as e:
		js = None

	if js is None or 'status' not in js or js['status'] != 'OK':
		print('==== Failure to Retrieve ====')
		print(data)
		continue

	print(json.dumps(js, indent=4))

	latitude = js["results"][0]["geometry"]["location"]["lat"]
	longitude = js["results"][0]["geometry"]["location"]["lng"]
	print('latitude: ', latitude, '\tlongitude: ', longitude)
	location = js['results'][0]['formatted_address']
	print(location)



	