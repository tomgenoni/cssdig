import os, re, urllib2, time, datetime, operator, sys, gzip
from urlparse import urlparse, urlunparse

url = urlparse('http://www.foo.com')
css = urlparse('/asset/style.css?fds=adf')

query_string = ""
if not css.query == "":
    query_string = "?" + css.query

print urlunparse((css.scheme or url.scheme, css.netloc or url.netloc, os.path.join(os.path.dirname(url.path), css.path + query_string), None, None, None))
