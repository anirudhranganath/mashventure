import flickr_keys
import flickr_api
import urllib
from urllib2 import *
import xml.etree.ElementTree as ET
import xml.etree as etree

def get_carousel_images_by_location(location):
    flickr_api.set_keys(api_key = flickr_keys.api_key, api_secret = flickr_keys.api_secret)
    url = "http://api.flickr.com/services/rest/?%s"
    query_params = urllib.urlencode({"method":"flickr.photos.search","api_key":flickr_keys.api_key,"tags":location,"per_page":20})
    print url%query_params
    #url = "http://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=%s&tags=joshua+tree&safe_search=1&per_page=20"%flickr_keys.api_key;
    result = urlopen(url%query_params)
    tree = ET.parse(result).getroot()
    imageURL = [];
    carouselList = [];
    photoTags = tree.findall("photos")[0].getchildren()
    #print photoTags[0].attrib['title']
    for x in photoTags:
      imageURL.append("http://farm"+x.attrib['farm']+".staticflickr.com/"+x.attrib['server']+"/"+x.attrib['id']+"_"+x.attrib['secret']+".jpg")
    for imgurl in imageURL:
      carouselList.append('<div class="item"><img width="900" height="500" data-src="holder.js/900x500/auto/#777:#555/text:First slide" src="'+imgurl+'"></div>')
    return carouselList

