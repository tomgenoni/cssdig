from bs4 import BeautifulSoup
import urllib2

css_combined = ""

html_doc = urllib2.urlopen('http://www.apple.com/').read()
soup = BeautifulSoup(html_doc)

for link in soup.find_all('link'):
    link_href = link.get('href')
    if link_href.endswith('.css'):
        css_combined += urllib2.urlopen(link_href).read()
