from urlparse import urlparse
from collections import OrderedDict
from collections import Counter
from bs4 import BeautifulSoup
import re, urllib2, time, datetime, operator, sys

url = "https://medium.com/the-lauren-papers/a30ac0d4b1d0"

domain_blacklist = [
    'cloud.typography.com'
]

css_urls = []
css_combined = ""

html_doc = urllib2.urlopen(url).read()
soup = BeautifulSoup(html_doc)

# Find all <link> elements.
for link in soup.find_all('link'):
    # Get the href attr of the <link>.
    if link.get('rel')[0] ==  'stylesheet':
        # If it's a stylesheet, get the link to the css sheet.
        link_href = link.get('href')
        # If it starts with an absolute path, construct final css path.
        if link_href.startswith("/"):
            link_href = url + link_href
        # If it starts with an relative path, construct final css path.
        elif link_href.startswith("."):
            link_href = url + "/" + link_href

        print link_href

        #Create list of CSS files on the page.
        css_urls.append(link_href)


# Concatenate all CSS files into one long string, only if they are not blacklisted.
for u in css_urls:
    host = urlparse(u).hostname
    if not host in domain_blacklist:
        css_combined += urllib2.urlopen(u).read()


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
    'height'
]

build_dir = 'output'
build_file = build_dir+'/index.html'
layout_tmpl_html = open('template/index.tmpl').read()

html = "<table class='stats'><tr><td><b>CSS File:</b></td><td><a href='TODO'/>TODO</a></td></tr>\n"
html += "<tr><td><b>Created:</b></td><td>"+timestamp+"</td></tr></table>\n"

# Find all instances of !important
imp_values = re.findall("!important", css_combined)
html += "<table>\n"
html += "<tr class='totals'>\n<td>!important</td>" + "<td>" + str(len(imp_values)) + "</td>\n</tr>\n"
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
