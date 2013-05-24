from collections import OrderedDict
from collections import Counter
import urllib2
import operator
import re
import sys
from urlparse import urlparse
search_values = [
    '!important',
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

css_link = sys.argv[1]
css = urllib2.urlopen(css_link).read()

parsed_uri = urlparse(css_link)
css_domain = parsed_uri[1]

html = "<h1>CSS Report for " + css_domain + "</h1>"
html += "<p><a href='"+css_link+"'/>"+css_link+"</a></p>\n"

for s in search_values:

    result = re.findall("(?<!-)" + s + "(.*?):(.*?)[;|}]", css)
    if not result:
        result = re.findall("!important", css)
    result.sort()
    cnt = Counter(result)
    html += "<table>\n"
    html += "<tr class='totals'>\n<td>"+s+"</td>" + "<td>" + str(len(result)) + "</td>\n</tr>\n"
    for key, value in sorted(cnt.iteritems(), key=lambda (k,v): (k,v)):
        color_example = ""
        key = key.lstrip()
        if s == "color":
            color_example = "<span class='color-example' style='background:"+key+"'></span>"
        if key != "!important":
            html += "<tr>\n<td>" + color_example  + s +": " + "%s;</td><td>%s</td>\n</tr>\n" % (key, value)
    html += "</table>\n"

tf = open(build_file, 'w')
final_output = layout_tmpl_html.replace("{{ results }}", html)
tf.write(final_output)
tf.close