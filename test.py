import posixpath
from urlparse import urlparse, urljoin, urlunparse

def expand_url(home, url):
    join = urljoin(home,url)
    url2 = urlparse(join)
    path = posixpath.normpath(url2[2])

    return urlunparse(
        (url2.scheme,url2.netloc,path,url2.params,url2.query,url2.fragment)
    )

print expand_url('http://www.huffingtonpost.com/', 'http://s.huffpost.com/assets/css.php?f=hp_modules%2Fmodule.threeup.css%2Cemail_share.css%2Ccommercial.css%2Csite_promo.css%2Cpoll_like.css%2Csearch_autocomplete.css%2Csocial-navbar.css%2Chighlights.css%2Chp_modules%2Fmodule.apps_feeds.css%2Chufflists.css%2Cdirect_message.css%2Cshare_boxes.css%2Cbadges_v2.css%2Csharer.css%2Chp_modules%2Fmodule.snn_entry_inside.css%2Chp_modules%2Fmodule.most_popular_social.css%2Chp_modules%2Ffacebook.css%2Chp_modules%2Fmodule.most_popular_celebrity.css%2Cuser_levels.css&amp;v=1369407084')