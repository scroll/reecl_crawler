from bs4 import BeautifulSoup
from collections import OrderedDict
import csv
import requests

page = 'http://reecl.org/category/%D0%B4%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%87%D0%B8%D1%86%D0%B8-%D0%B8-%D0%B8%D0%B7%D0%BF%D1%8A%D0%BB%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D0%B8/%D0%B8%D0%B7%D0%BF%D1%8A%D0%BB%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D0%B8-%D0%BF%D1%80%D0%BE%D0%B7%D0%BE%D1%80%D1%86%D0%B8/page/'

output_file = '/home/marin.petrov/workspace/reecl_crawler/output.csv'
output_data = OrderedDict()

def extract_email(mailtos):
    for i in mailtos:
        href=i['href']
        try:
            str1, str2 = href.split(':')
        except ValueError:
            return ''
        
        return str2

print 'Starting to crawl...'
for i in range(200): # random large enough number of pages
    r = requests.get('{}{}/'.format(page,i))
    if r.status_code == 404:
        break

    soup = BeautifulSoup(r.text, 'html.parser')
    ul = soup.find("ul", id="listlatestnews")
    # These are all the list elements on the page
    li = ul.find_all('li')

    # We iterate through each company
    for company in li:
        company_row = []
        company_name = company.find('a', rel="bookmark").text
        company_row.append(company_name)
        company_email = company.select('a[href^=mailto:]')
        company_row.append(extract_email(company_email))
        company_websites = company.select('a[href^=http:]')
        for site in company_websites:
            company_row.append(site['href'])

        print company_row
        output_data[company_name] = company_row
        
print 'Dumping to file...'
with open(output_file, 'a') as csv_file:
    writer = csv.writer(csv_file)
    for company in output_data:
        writer.writerow([unicode(s).encode("utf-8") for s in output_data[company]])
print 'Done!'

