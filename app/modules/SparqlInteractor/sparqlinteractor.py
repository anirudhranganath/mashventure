from SPARQLWrapper import SPARQLWrapper, JSON


sesame_query_endpoint = "http://localhost:8080/openrdf-sesame/repositories/mashtrial"
sesame_update_endpoint = sesame_query_endpoint + "/update"


def update_query(query_string):
    sparql = SPARQLWrapper(sesame_update_endpoint)
    sparql.setQuery(query_string)
    sparql.method = 'POST'
    sparql.query()


def insert(query_string):
    update_query(query_string)


def query(query_string):
    sparql = SPARQLWrapper(sesame_query_endpoint)
    sparql.setQuery(query_string)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results