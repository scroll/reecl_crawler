import requests
from bs4 import BeautifulSoup

page = 'http://reecl.org/category/%D0%B4%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%87%D0%B8%D1%86%D0%B8-%D0%B8-%D0%B8%D0%B7%D0%BF%D1%8A%D0%BB%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D0%B8/%D0%B8%D0%B7%D0%BF%D1%8A%D0%BB%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D0%B8-%D0%BF%D1%80%D0%BE%D0%B7%D0%BE%D1%80%D1%86%D0%B8/page/'

for i in range(200): # random large enough number of pages
    r = requests.get('{}{}/'.format(page,i))
    if r.status_code == 404:
        break
    
    

# soup = BeautifulSoup(r.text, 'html.parser')

# ul = soup.find("ul", id="listlatestnews")

# li = ul.find_all('li')

# href = li[1].find_all('a')
# print href[-1]['href']
