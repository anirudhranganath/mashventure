import urllib
from app.modules.SparqlInteractor import search as spqlsearch

def user_form_search(location):
    results = spqlsearch.get_recarea_details_from_name(location)
    '''
    ret = []
    for result in results:
        ret.append([results['RecAreaName'], results['RecAreaID']])
    '''
    return [[results['RecAreaName'], results['RecAreaID'],urllib.urlencode({"site":location})]]