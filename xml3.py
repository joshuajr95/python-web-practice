import xml.etree.ElementTree as ET

string = None

with open('practice.xml', 'r') as fileHandle:
	string = fileHandle.read()

xmlTree = ET.fromstring(string)

elemList = xmlTree.findall('list/element')


i = 1
print("\n")
for element in elemList:
	print("Person ", i)
	print("==================")
	print('First Name: ', element.find('firstname').text)
	print('Last Name: ', element.find('lastname').text)
	print('Age: ', element.find('age').text)
	print('ID Number: ', element.find('id').text)
	print("\n")
	i += 1
