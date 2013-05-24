from urlparse import urlparse
from collections import OrderedDict
from collections import Counter
from bs4 import BeautifulSoup
import re, urllib2, time, datetime, operator, sys

url = "https://medium.com/the-lauren-papers/a30ac0d4b1d0"

print urllib2.urlopen(url).read()
