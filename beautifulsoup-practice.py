import urllib.request
from bs4 import BeautifulSoup


url = input("Enter URL to scrape: ")

htmlResponse = urllib.request.urlopen(url)

soup = BeautifulSoup(htmlResponse, 'html.parser')

print(soup.prettify())
print("\n\n")
print(soup.title)
print("\n\nLinks in the page")



# soup.find_all('a') is equivalent to soup('a')
for link in soup.find_all('a'):
	print(link.get('href'))

print("\n\n")
