from app.modules.SparqlInteractor import search as spqlsearch
from app.modules.FlickrInteractor import FlickrImages
from app.modules.Weather import SimpleWeather
import UserFormSearch

def page_info(name):
    results = {"sparqlresults":spqlsearch.get_recarea_details_from_name(name),"flickrcarousel":FlickrImages.get_carousel_images_by_location(name)}
    [lat,lon] = UserFormSearch.decodeAddressToCoordinates(name)
    results["simpleweather"] = SimpleWeather.get_weather(lat,lon)
    return  results
