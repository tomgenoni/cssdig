import urllib2
import gzip
from cStringIO import StringIO

url = "https://dnqgz544uhbo8.cloudfront.net/_/fp/css/main-base.3oVpaIFFn_9laeEJwwsA2Q.css"


response = urllib2.urlopen(url)
if response.info().get('Content-Encoding') == 'gzip':
    buf = StringIO( response.read())
    f = gzip.GzipFile(fileobj=buf)
    print f.read()
