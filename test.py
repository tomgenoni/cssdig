from urlparse import urlparse

parser.setFetcher(fetcher)
sheet = parser.parseFile('report.css', 'ascii')
print sheet.cssText
