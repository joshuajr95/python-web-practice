import json

data = '''
[
	{
	"id" : "001",
	"x" : "2",
	"name" : "Josh"
	},
	{
	"id" : "009",
	"x" : "7",
	"name" : "Noah"
	}
]'''

info = json.loads(data)
print('User count: ', len(info))
print("\n")

for item in info:
	print('Name: ', item['name'])
	print('ID Number: ', item['id'])
	print('Attribute: ', item['x'])
	print("\n")
