# def application(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/plain')])
#     return environ['wsgi.input']


import os, re, urllib2, time, datetime, operator, sys, gzip, json
from urlparse import urlparse, urljoin, urlunparse
from bs4 import BeautifulSoup
from cStringIO import StringIO

def application(environ, start_response):
    start_response('200 OK', [ ('Content-type', 'application/json; charset=utf-8') ])
    url = environ['wsgi.input'].read()

    req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
    doc = urllib2.urlopen(req)
    if doc.info().get('Content-Encoding') == 'gzip':
        buf = StringIO(doc.read())
        f = gzip.GzipFile(fileobj=buf)
        content = f.read()
    else:
        content = doc.read()

    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%B %d, %Y at %H:%M:%S')

    # Domains that can't or shouldn't be included.
    domain_blacklist = [
        'use.typekit.com',
        'fonts.googleapis.com',
        'cloud.webtype.com'
    ]

    # Parse the url.
    url_parsed = urlparse(url)

    css_urls_all = []
    css_urls_clean = []
    css_urls_bad = []
    css_combined = ""

    def getRemoteURL(url):
        req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
        doc = urllib2.urlopen(req)
        if doc.info().get('Content-Encoding') == 'gzip':
            buf = StringIO(doc.read())
            f = gzip.GzipFile(fileobj=buf)
            return f.read()
        else:
            return doc.read()

    soup = BeautifulSoup(getRemoteURL(url), "lxml")

    # Find all <link> elements.
    for link in soup.find_all('link'):
        # Get the rel attr of the <link>.
        rel = link.get('rel')[0]
        if rel.lower() == 'stylesheet':

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
                req = urllib2.Request(u, headers={'User-Agent' : "Magic Browser"})
                doc = urllib2.urlopen(req)
                if doc.info().get('Content-Encoding') == 'gzip':
                    buf = StringIO(doc.read())
                    f = gzip.GzipFile(fileobj=buf)
                    css_combined += f.read()
                else:
                    css_combined += doc.read()
                css_urls_clean.append(u)
            except urllib2.HTTPError, e:
                css_urls_bad.append(u)

    # Check for styles in head.
    style_css = ''.join([s.get_text() for s in soup.find_all('style')])
    if not style_css:
        css_combined = css_combined + style_css

    # remove comments - this will break a lot of hacks :-P
    css_combined = re.sub( r'\s*/\*\s*\*/', "$$HACK1$$", css_combined ) # preserve IE<6 comment hack
    css_combined = re.sub( r'/\*[\s\S]*?\*/', "", css_combined )
    css_combined = css_combined.replace( "$$HACK1$$", '/**/' ) # preserve IE<6 comment hack

    # spaces may be safely collapsed as generated content will collapse them anyway
    css_combined = re.sub( r'\s+', ' ', css_combined )

    # add semicolon if needed
    css_combined = re.sub(r'([a-zA-Z0-9])\s*?}', r'\g<1>'+';}', css_combined )


    output = { "css_combined" : css_combined, "css_urls_clean" : css_urls_clean , "css_urls_bad" : css_urls_bad }
    output = json.dumps(output)

    return output