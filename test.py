import re
import urllib2

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

css = urllib2.urlopen("http://www.regular-expressions.info/regex.css").read()

for p in props:
    regex = "(?<!-)"+p+".*?:(.*?)[;|}]"
    values = re.findall(regex, css)

    for value in values:
        print p + ": " + value.lstrip() + ";"

