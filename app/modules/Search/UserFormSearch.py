import urllib
import urllib2
import json
import StringIO
from math import sin, cos, sqrt, atan2, radians
from operator import itemgetter
from app.modules.SparqlInteractor import search as spqlsearch

def user_form_search_location(location):
    results = spqlsearch.get_recarea_details_from_name(location)
    '''
    ret = []
    for result in results:
        ret.append([results['RecAreaName'], results['RecAreaID']])
    '''
    return [[results['RecAreaName'], results['RecAreaID'],urllib.urlencode({"site":location})]]

def decodeAddressToCoordinates( address ):
    #credit http://stackoverflow.com/questions/15285691/googlemaps-api-address-to-coordinates-latitude-longitude
  urlParams = {'address': address,'sensor': 'false'}
  url = 'http://maps.google.com/maps/api/geocode/json?' + urllib.urlencode( urlParams )
  response = urllib2.urlopen( url )
  responseBody = response.read()
  body = StringIO.StringIO( responseBody )
  result = json.load( body )
  if 'status' not in result or result['status'] != 'OK':
    return None
  else:
    #return {'lat': result['results'][0]['geometry']['location']['lat'],'lng': result['results'][0]['geometry']['location']['lng']}
    return [result['results'][0]['geometry']['location']['lat'],result['results'][0]['geometry']['location']['lng']]

def distance(point1,point2):
    #credit http://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude-python
    R = 6373.0
    lat1 = radians(float(point1[0]))
    lon1 = radians(float(point1[1]))
    lat2 = radians(float(point2[0]))
    lon2 = radians(float(point2[1]))
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    dist = R * c
    return dist

def user_form_search_activity_location(activity,location):
    location_lat_long = decodeAddressToCoordinates(location)
    if activity =='':
        activity = "CAMPING"
    rec_id_lat_long = spqlsearch.get_rec_id_lat_long_for_activity(activity)
    for rec_area in rec_id_lat_long:
        rec_area.append(distance(location_lat_long,[rec_area[1],rec_area[2]]))
    rec_id = sorted(rec_id_lat_long, key=itemgetter(3))
    rec_id = rec_id[0:50]
    print rec_id
    ret = []
    for rec_area in rec_id:
        ret.append([rec_area[0],False,urllib.urlencode({"site":rec_area[0].encode('utf-8')})])
    return ret
