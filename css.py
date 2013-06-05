import os, re, urllib2, time, datetime, operator, sys, gzip, tinyurl

#css = urllib2.urlopen("http://z.cdn.turner.com/cnn/tmpl_asset/static/www_homepage/2495/css/hplib-min.css").read()
css = ".foo { width: 10px; } .bar { width: 5px; height:    10px }"

# remove comments - this will break a lot of hacks :-P
css = re.sub( r'\s*/\*\s*\*/', "$$HACK1$$", css ) # preserve IE<6 comment hack
css = re.sub( r'/\*[\s\S]*?\*/', "", css )
css = css.replace( "$$HACK1$$", '/**/' ) # preserve IE<6 comment hack

# spaces may be safely collapsed as generated content will collapse them anyway
css = re.sub( r'\s+', ' ', css )

# add semicolon if needed
css = re.sub(r'([a-z0-9]\s+)(})', r'\g<1>'+';'+r'\g<2>', css )

print css