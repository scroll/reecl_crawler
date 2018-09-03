from bs4 import BeautifulSoup
import csv
from datetime import datetime
import requests


page = 'http://reecl.org/category/%D0%B4%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%87%D0%B8%D1%86%D0%B8-%D0%B8-%D0%B8%D0%B7%D0%BF%D1%8A%D0%BB%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D0%B8/%D0%B8%D0%B7%D0%BF%D1%8A%D0%BB%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D0%B8-%D0%BF%D1%80%D0%BE%D0%B7%D0%BE%D1%80%D1%86%D0%B8/page/'

output = '/home/marin.petrov/workspace/reecl_crawler/output.csv'

output_data = set()

for i in range(200): # random large enough number of pages
    r = requests.get('{}{}/'.format(page,i))
    if r.status_code == 404:
        break

    soup = BeautifulSoup(r.text, 'html.parser')
    ul = soup.find("ul", id="listlatestnews")
    # These are all the list elements on the page
    li = ul.find_all('li')

    for elem in li:
        a = elem.find_all('a')
        output_data.add(a[-1]['href'])


print output_data
# with open(output, 'a') as csv_file:
#     writer = csv.writer(csv_file)
#     for row in output_data:
#         writer.writerow([row])
