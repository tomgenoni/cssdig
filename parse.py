import os, re, urllib2, time, datetime, operator, sys, gzip
from urlparse import urlparse, urljoin, urlunparse
from collections import OrderedDict
from collections import Counter
from bs4 import BeautifulSoup
from cStringIO import StringIO

url = "http://www.huffingtonpost.com/"

# Domains that can't be accessed by the script.
domain_blacklist = [
    'cloud.typography.com',
    'use.typekit.com',
    'fonts.googleapis.com'
]

# Parse the url.
orig = urlparse(url)

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
        link_href = urlparse(link.get('href'))

        # Resolve the path to the CSS files.
        full_css_path = urlunparse((link_href.scheme or orig.scheme, link_href.netloc or orig.netloc, os.path.join(os.path.dirname(orig.path), link_href.path + "?" + link_href.query), None, None, None))

        #Create list of CSS files on the page.
        css_urls.append(full_css_path)

for u in css_urls:
    host = urlparse(u).hostname
    # Concatenate all CSS files into one long string if they are not blacklisted.
    if not host in domain_blacklist:
        css_combined += getRemoteURL(u)

props = [
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

ts = time.time()
timestamp = datetime.datetime.fromtimestamp(ts).strftime('%m-%d-%Y at %H:%M:%S')

# Star collecting the HTML.
html = "<table class='stats'><tr><td><b>CSS File:</b></td><td><a href='TODO'/>TODO</a></td></tr>\n"
html += "<tr><td><b>Created:</b></td><td>"+timestamp+"</td></tr></table>\n"

# Find all instances of !important
important_values = re.findall("!important", css_combined)
html += "<table>\n"
html += "<tr class='totals'>\n<td>!important</td>" + "<td>" + str(len(important_values)) + "</td>\n</tr>\n"
html += "</table>\n"

for p in props:
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

tf = open(build_file, 'w')
final_output = layout_tmpl_html.replace("{{ results }}", html)
tf.write(final_output)
tf.close
