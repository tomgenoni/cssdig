from collections import OrderedDict
from collections import Counter
import re, urllib2, time, datetime, operator, sys

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

css_link = "http://www.gap.com/gzip_N1274944906/optimizedBundles/globalOptimized.css"
css = urllib2.urlopen(css_link).read()

html = "<p><a href='"+css_link+"'/>"+css_link+"</a></p>\n"
html += "<p class='time'>Created " + timestamp + "</p>\n"

# Find all instances of !important
imp_values = re.findall("!important", css)
html += "<table>\n"
html += "<tr class='totals'>\n<td>!important</td>" + "<td>" + str(len(imp_values)) + "</td>\n</tr>\n"
html += "</table>\n"

for p in props:
    regex = "(?<!-)"+p+".*?:(.*?)[;|}]"
    values = re.findall(regex, css)
    values.sort()
    cnt = Counter(values)

    html += "<table>\n"
    html += "<tr class='totals'>\n<td>"+p+"</td>" + "<td>" + str(len(values)) + "</td>\n</tr>\n"

    for key, value in sorted(cnt.iteritems(), key=lambda (k,v): (k,v)):
        color_example = ""
        key = key.lstrip()
        html += "<tr>\n<td>" + p +": " + "%s;</td><td>%s</td>\n</tr>\n" % (key, value)
    html += "</table>\n"

tf = open(build_file, 'w')
final_output = layout_tmpl_html.replace("{{ results }}", html)
tf.write(final_output)
tf.close
