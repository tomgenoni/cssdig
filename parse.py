import os, re, urllib2, time, datetime, operator, sys, gzip
from urlparse import urlparse, urljoin, urlunparse
from collections import OrderedDict
from collections import Counter
from bs4 import BeautifulSoup
from cStringIO import StringIO

url = "http://www.twitter.com/"
#url = "http://atomeye.com"

# Domains that can't or shouldn't be included.
domain_blacklist = [
    'cloud.typography.com',
    'use.typekit.com',
    'fonts.googleapis.com'
]

# Properties to be tested.
properties = [
    'background',
    'border',
    'color',
    'font',
    'font-size',
    'font-family',
    'font-weight',
    'line-height',
    'margin',
    'margin-left',
    'margin-right',
    'padding',
    'padding-left',
    'padding-right',
    'width',
    'height',
    'z-index'
]

build_dir = 'output'
build_file = build_dir+'/index.html'
layout_tmpl_html = open('template/index.tmpl').read()

# Get timestamp.
ts = time.time()
timestamp = datetime.datetime.fromtimestamp(ts).strftime('%m-%d-%Y at %H:%M:%S')


# Parse the url.
url_parsed = urlparse(url)

css_urls = []
css_combined = ""

def getRemoteURL(url):
    doc = urllib2.urlopen(url)
    if doc.info().get('Content-Encoding') == 'gzip':
        buf = StringIO(doc.read())
        f = gzip.GzipFile(fileobj=buf)
        return f.read()
    else:
        return doc.read()

soup = BeautifulSoup(getRemoteURL(url))

# Find all <link> elements.
for link in soup.find_all('link'):
    # Get the rel attr of the <link>.
    if link.get('rel')[0] ==  'stylesheet':

        # If it's a stylesheet, get the link to the css sheet.
        css_href_parsed = urlparse(link.get('href'))

        # Test for query string, include only if needed.
        query_string = None
        if not css_href_parsed.query == None:
            query_string = "?" + css_href_parsed.query

        # Resolve the path to the CSS files.
        full_css_path = urlunparse((css_href_parsed.scheme or url_parsed.scheme, css_href_parsed.netloc or url_parsed.netloc, os.path.join(os.path.dirname(url_parsed.path), css_href_parsed.path + query_string), None, None, None))

        #Create list of CSS files on the page.
        css_urls.append(full_css_path)

# Go through all the css paths.
for u in css_urls:
    host = urlparse(u).hostname
    # Concatenate all CSS files into one long string if they are not blacklisted.
    if not host in domain_blacklist:
        css_combined += getRemoteURL(u)

# Start collecting the HTML.
html = "<table class='stats'><tr><td><b>CSS File:</b></td><td><a href='TODO'/>TODO</a></td></tr>\n"
html += "<tr><td><b>Created:</b></td><td>"+timestamp+"</td></tr></table>\n"

# Find all instances of !important.
important_values = re.findall("!important", css_combined)
html += "<table>\n"
html += "<tr class='totals'>\n<td>!important</td>" + "<td>" + str(len(important_values)) + "</td>\n</tr>\n"
html += "</table>\n"

# Run through all the properties.
for p in properties:
    regex = "(?<!-)"+p+"\s*:\s*(.*?)[;|}]"
    values = re.findall(regex, css_combined)
    values.sort()
    cnt = Counter(values)

    html += "<table>\n"
    html += "<tr class='totals'>\n<td>"+p+"</td>" + "<td>" + str(len(values)) + "</td>\n</tr>\n"

    for key, value in sorted(cnt.iteritems(), key=lambda (k,v): (k,v)):
        color_example = ""
        key = key.lstrip()
        if p == "color" or p == "background":
            color_example = "<span class='color-example' style='background:"+key+"'></span>"
        html += "<tr>\n<td>" + color_example + p +": " + "%s;</td><td>%s</td>\n</tr>\n" % (key, value)
    html += "</table>\n"

# Open build file, replace placeholders.
tf = open(build_file, 'w')
final_output = layout_tmpl_html.replace("{{ results }}", html)
tf.write(final_output)
tf.close