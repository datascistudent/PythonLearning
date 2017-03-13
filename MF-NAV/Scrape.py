__author__ = 'gkannappan'

'''
import urllib2
from pprint import pprint
from bs4 import BeautifulSoup

fw = open(r"/Users/gkannappan/desktop/MF.txt", 'a+')

url = "http://morningstar.in/mutualfunds/f0gbr06r5e/reliance-tax-saver-(elss)-fund-growth/overview.aspx"
url2 = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' })
pprint(url)
f = urllib2.urlopen(url2)
    #f = urllib2.urlopen('http://www.amazon.com/product-reviews/B01617VPUY')
page=f.read().lower()#; print '%s'%(page.count('product-reviews'))
soup = BeautifulSoup(page, "lxml")
print  >> fw, soup.prettify().encode('utf-8')
'''

import urllib2
import pprint
from bs4 import BeautifulSoup
import csv
import codecs
import cStringIO
class DictUnicodeWriter(object):
    def __init__(self, f, fieldnames, encoding="utf-8"):
        # Redirect output to a queue
        self.queue = cStringIO.StringIO()
        self.writer = csv.DictWriter(self.queue, fieldnames, lineterminator = '\n')
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()
    def writerow(self, D):
        self.writer.writerow({k:v.encode("utf-8") for k,v in D.items()})
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        data = self.encoder.encode(data)
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)
    def writerows(self, rows):
        for D in rows:
            self.writerow(D)
    def writeheader(self):
        self.writer.writeheader()

rev_date_header = 'Date'
rev_title_header = 'Title'
rev_rate_header = 'Rate'
rev_text_header = 'Text'
rev_vote_header = 'Votes'
csvfile = open("/Users/gkannappan/desktop/MF.csv", "w")
csvfile.truncate()
csvwriter = DictUnicodeWriter(csvfile,[rev_date_header, rev_title_header, rev_rate_header, rev_text_header, rev_vote_header])
# csvWriter = UnicodeWriter(csvfile, fieldnames=fieldnames, delimiter =' ',quotechar =',',quoting=csv.QUOTE_MINIMAL)
csvwriter.writeheader()


#url = "http://morningstar.in/mutualfunds/f0gbr06r5e/reliance-tax-saver-(elss)-fund-growth/overview.aspx"
url = "https://www.valueresearchonline.com/funds/newsnapshot.asp?schemecode=10826&utm_source=direct-click&utm_medium=funds&utm_term=axis+lon&utm_content=Axis+Long+Term+Equity&utm_campaign=vro-search"
url2 = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' })
print(url)
f = urllib2.urlopen(url2)

print '-'*40



def bs4_element_to_list(el, pos):
    elmt = el[pos].contents
    return elmt

fullHTML = BeautifulSoup(f,'html.parser')

for NAV_Date in fullHTML.find_all('div', {'class' : 'pull-left change-date'}):
    date = NAV_Date.contents
    nav_date = date[0].encode('ascii').strip()
    nav_date = nav_date.replace("\n", " ")
    print nav_date
    #print str.replace(nav_date, 'Change from previous, NAV as on', '')

for NAV_List in fullHTML.find_all('div', {'class' : 'pull-left fund-type'}):
    nav_element = NAV_List.find_all('li')
    #print '*****'
    nav_1= bs4_element_to_list(nav_element,0)
    nav_2= bs4_element_to_list(nav_element,1)
    print nav_1[0].strip(), nav_1[2].strip(), nav_2[0].strip(), nav_2[2].strip()
    #print '*****'
        #csvwriter.writerow({'NAV Today':NAV})
csvfile.close()