import os, re, urllib2, time, datetime, operator, sys, gzip, tinyurl
import tinycss

properties = []

css = urllib2.urlopen('http://localhost/css-dig/assets/styles.css').read()

parser = tinycss.make_parser()

for r in parser.parse_stylesheet(css).rules:
    for d in r.declarations:
        properties.append(d.name)

properties = list(set(properties))
properties.sort()

for p in properties:
    print p