import json


# json data here contains a dictionary of values
data = '''{
	"name" : "Josh",
	"phone" : {
		"type" : "intl",
		"number" : "+1 802 299 9743"
	},
	"email" : {
	"hide" : "yes"
	}
}'''

info = json.loads(data)
print('Name: ', info["name"])
print('Hide: ', info["email"]["hide"])