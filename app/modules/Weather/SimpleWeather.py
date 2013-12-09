import urllib,urllib2
import xml.etree.ElementTree as ET
import xml.etree as etree

def get_woeid(lat,lon):
    url = "http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20geo.placefinder%20where%20text%3D%22"+repr(lat)+"%2C"+repr(lon)+"%22%20and%20gflags%3D%22R%22"
    result = urllib2.urlopen(url)
    tree = ET.parse(result).getroot()
    return tree.findall('results')[0].findall('Result')[0].findall('woeid')[0].text

def get_weather(lat,lon):
    woeid = get_woeid(lat,lon)
    url = "http://weather.yahooapis.com/forecastrss?w=%s"%woeid
    result = urllib2.urlopen(url)
    tree = ET.parse(result).getroot()
    return '\n'.join(tree.findall('channel')[0].findall('item')[0].findall('description')[0].text.split('\n')[2:-3])