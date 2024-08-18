import requests
from bs4 import BeautifulSoup

f = open('list.html', 'r')
s = f.read()
soup = BeautifulSoup(s,"html.parser")

parks = soup.select('.areaBox')
for park in parks:
    a_item = parks.find_all("a")
    print(a_item)
