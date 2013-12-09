import urllib2
import urllib
import json

import active_keys

urlbase = "http://api.amp.active.com/v2/search?%s"

def search_query(activity,location):
    query_params = urllib.urlencode({"api_key":active_keys.search2_key,"query":query})
    req = urllib.urlopen(urlbase%query_params)
    print req.geturl()
    resp = req.read()
    print resp

