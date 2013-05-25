import urllib2
import gzip
from cStringIO import StringIO

url = "https://developer.mozilla.org/en-US/"


response = urllib2.urlopen(url)
if response.info().get('Content-Encoding') == 'gzip':
    buf = StringIO( response.read())
    f = gzip.GzipFile(fileobj=buf)
    print f.read()
