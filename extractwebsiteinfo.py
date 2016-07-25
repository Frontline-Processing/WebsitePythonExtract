import csv
import urllib2
from bs4 import BeautifulSoup

records = []
for index in range(39):
    url = get_url(index)
    response = urllib2.urlopen(url)
    try:
        hrml = reponse.read()
    except Exception:
        raise
    else:
        my_parse(html)
    finally:
        try:
            response.close()
        except (UnboundLocalError, NameError):
            raise UnboundLocalError
def my_parse(html):
    soup = BeautifulSoup(open("https://dev.frontlineprocessing.com/admin/structure/trigger/node"))
    table2= soup.find_all('table')[1]
    for tr in table2.find_all('tr')[2:]:
        tds = tr.find_all('td')
        url = tds[8].a.get('href')
        records.append([elem.text.encode('utf-8')) for elem in tds])

with open('listing.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(records)
