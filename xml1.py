import xml.etree.ElementTree as ET

data = '''
<person>
	<name>Josh</name>
	<phone type="intl">
		+1 802 299 9743
	</phone>
	<email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name: ', tree.find('name').text)
print('Attr: ', tree.find('email').get('hide'))