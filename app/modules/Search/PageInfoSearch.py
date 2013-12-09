from app.modules.SparqlInteractor import search as spqlsearch

def page_info(name):
    results = {"sparqlresults":spqlsearch.get_recarea_details_from_name(name)}
    return  results
