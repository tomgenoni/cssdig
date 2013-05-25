from collections import OrderedDict
from collections import Counter
from bs4 import BeautifulSoup
from cStringIO import StringIO
import urlparse, os, re, urllib2, time, datetime, operator, sys, gzip

url = "http://www.apple.com/"

# Domains that can't be accessed by the script.
domain_blacklist = [
    'cloud.typography.com',
    'use.typekit.com'
]

# Parse the url.
orig = urlparse.urlparse(url)

css_urls = []
css_combined = ""

html_doc = urllib2.urlopen(url).read()
soup = BeautifulSoup(html_doc)

# Find all <link> elements.
for link in soup.find_all('link'):
    # Get the href attr of the <link>.
    if link.get('rel')[0] ==  'stylesheet':
        # If it's a stylesheet, get the link to the css sheet.
        link_href = urlparse.urlparse(link.get('href'))

        # Resolve the path tot hte
        full_css_path = urlparse.urlunparse((link_href.scheme or orig.scheme, link_href.netloc or orig.netloc, os.path.join(os.path.dirname(orig.path), link_href.path), None, None, None))

        #Create list of CSS files on the page.
        css_urls.append(full_css_path)


for u in css_urls:
    host = urlparse.urlparse(u).hostname
    # Concatenate all CSS files into one long string, only if they are not blacklisted.
    if not host in domain_blacklist:
        response = urllib2.urlopen(u)
        #Check to see if URL is gziped.
        if response.info().get('Content-Encoding') == 'gzip':
            buf = StringIO( response.read())
            f = gzip.GzipFile(fileobj=buf)
            css_combined = f.read()
        else:
            css_combined = response.read()

ts = time.time()
timestamp = datetime.datetime.fromtimestamp(ts).strftime('%m-%d-%Y at %H:%M:%S')

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

html = "<table class='stats'><tr><td><b>CSS File:</b></td><td><a href='TODO'/>TODO</a></td></tr>\n"
html += "<tr><td><b>Created:</b></td><td>"+timestamp+"</td></tr></table>\n"

css_combined = "#globalheader { z-index:1; }"

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
