from bs4 import BeautifulSoup
import urllib2
import gzip
from cStringIO import StringIO

url = "http://gawker.com/"


response = urllib2.urlopen(url)




if response.info().get('Content-Encoding') == 'gzip':
    buf = StringIO( response.read())
    f = gzip.GzipFile(fileobj=buf)
    doc = f.read()
else:
    doc = response.read()

soup = BeautifulSoup(doc)

print doc