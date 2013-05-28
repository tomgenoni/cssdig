import os, re, urllib2, time, datetime, operator, sys, gzip, tinyurl
from urlparse import urlparse, urljoin, urlunparse
from collections import OrderedDict
from collections import Counter
from bs4 import BeautifulSoup
from cStringIO import StringIO

start_time = time.time()

# Get URL and properties from PHP
url = sys.argv[1]
properties = sys.argv[2].split(",")

# Uncomment to debug
# url = "http://en.wikipedia.org/wiki/Main_Page/"
# properties = ['background']

# Domains that can't or shouldn't be included.
domain_blacklist = [
    'use.typekit.com',
    'fonts.googleapis.com',
    'cloud.webtype.com'
]

# Get timestamp.
ts = time.time()
timestamp = datetime.datetime.fromtimestamp(ts).strftime('%B %d, %Y at %H:%M:%S')

# Parse the url.
url_parsed = urlparse(url)

css_urls_all = []
css_urls_clean = []
css_urls_bad = []
css_combined = ""
css_urls_list_good = ""
css_urls_list_bad = ""

def getRemoteURL(url):
    req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
    doc = urllib2.urlopen(req)
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
        query_string = ""
        if not css_href_parsed.query == "":
            query_string = "?" + css_href_parsed.query

        # Resolve the path to the CSS files.
        full_css_path = urlunparse((css_href_parsed.scheme or url_parsed.scheme, css_href_parsed.netloc or url_parsed.netloc, os.path.join(os.path.dirname(url_parsed.path), css_href_parsed.path + query_string), None, None, None))

        #Create list of CSS files on the page.
        css_urls_all.append(full_css_path)

# Go through all the css paths.
for u in css_urls_all:
    host = urlparse(u).hostname
    # Concatenate all CSS files into one long string if they are not blacklisted.
    if not host in domain_blacklist:
        try:
            doc = urllib2.urlopen(u)
            if doc.info().get('Content-Encoding') == 'gzip':
                buf = StringIO(doc.read())
                f = gzip.GzipFile(fileobj=buf)
                css_combined += f.read()
            else:
                css_combined += doc.read()
            css_urls_clean.append(u)
        except urllib2.HTTPError, e:
            css_urls_bad.append(u)

# Find all instances of !important.
important_values = re.findall("!important", css_combined)
html = "<div class='table-wrap'>\n"
html += "<table>\n"
html += "<tr class='totals'>\n<td>!important</td>" + "<td>" + str(len(important_values)) + "</td>\n</tr>\n"
html += "</table>\n"
html += "</div>\n"

# Run through all the properties.
for p in properties:
    regex = "(?<!-)"+p+"\s*:\s*(.*?)[;|}]"
    values = re.findall(regex, css_combined)
    values.sort()
    cnt = Counter(values)

    html += "<div class='table-wrap'>\n"
    html += "<table>\n"
    html += "<tr class='totals'>\n<td>"+p+"</td>" + "<td>" + str(len(values)) + "</td>\n</tr>\n"

    for key, value in sorted(cnt.iteritems(), key=lambda (k,v): (k,v)):
        color_example = ""
        key = key.lstrip()
        if p == "color" or p == "background":
            color_example = "<span class='color-example' style='background:"+key+"'></span>"
        html += "<tr>\n<td>" + color_example + p +": " + "%s;</td><td>%s</td>\n</tr>\n" % (key, value)
    html += "</table>\n"
    html += "</div>\n"

for u in css_urls_clean:
    css_urls_list_good += "<li><a href='"+u+"'>" + u + "</a></li>"

report_url = "http://cssdig.com/?url=" + url
for p in properties:
    report_url += "&p[]=" + p

if css_urls_bad:
    for b in css_urls_bad:
        css_urls_list_bad += "<li><a href='"+b+"'>" + b + "</a></li>"

# report_url = urllib2.quote(report_url.encode("utf8"))
report_tinyurl = tinyurl.create_one(report_url)

# Time elapsed
time_elapsed = time.time() - start_time
time_elapsed = str(round(time_elapsed,1))

# Start collecting the HTML.
header = "<div class='stats'>\n"
header += "<table>\n"
header += "<tr><td>URL Dug</td><td><a href='"+url+"'/>"+url+"</a></td></tr>\n"
header += "<tr><td>CSS Dug</td><td><ul>" + css_urls_list_good + "</ul></td></tr>\n"
if css_urls_bad:
    header += "<tr><td>Skipped</td><td><ul class='unparsed'>" + css_urls_list_bad + "</ul></td></tr>\n"
header += "<tr><td>This Dig</td><td><a href='"+report_tinyurl+"'/>"+report_tinyurl+"</a></td></tr>\n"
header += "<tr><td>Dug</td><td>"+timestamp+" taking "+time_elapsed+" seconds</td></tr>\n"
header += "</table>\n"
header += "</div>\n"

print header + html