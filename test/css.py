#!/usr/bin/python
# -*- coding: utf-8 -*-

import tinycss, urllib2

#css = urllib2.urlopen("http://atomeye.com/assets/css/style.css").read()
#css = urllib2.urlopen("http://localhost/css-dig/test/msn.css").read()



parser = tinycss.make_parser()
stylesheet = parser.parse_stylesheet_bytes(b'''

p.error { color: red } @media screen and (max-width: 1024px) { { size: landscape } }

''')

print stylesheet.rules

# for r in stylesheet.rules:
#     if hasattr(r, 'declarations'):
#         for d in r.declarations:
#             print d.name

#     if hasattr(r, 'media'):
#         for r in r.rules:
#             for d in r.declarations:
#                 print d.name
