import os, re, urllib2, time, datetime, operator, sys, gzip
import tinycss
css = urllib2.urlopen('http://atomeye.com/assets/css/style.css').read()

css = '''
@media print{#feed-link-text{display:none;}
'''

properties = []
parser = tinycss.make_parser()

for r in parser.parse_stylesheet(css).rules:
    for d in r.declarations:
        properties.append(d.name)

properties = list(set(properties))
properties.sort()

print properties