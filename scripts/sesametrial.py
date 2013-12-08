from SPARQLWrapper import SPARQLWrapper2, JSON

'''
sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery("""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?label
    WHERE { <http://dbpedia.org/resource/Asturias> rdfs:label ?label }
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

print results

for result in results["results"]["bindings"]:
    print(result["label"]["value"])

'''
#'''
sparql = SPARQLWrapper2("http://localhost:8080/openrdf-sesame/repositories/mashtrial")
sparql.setQuery("SELECT ?subj ?prop ?o WHERE { ?subj ?prop ?o. }")
#sparql.setReturnFormat(JSON)
results = sparql.query().convert()
print results
print results.variables  # this is an array consisting of "subj" and "prop"
for binding in results.bindings :
    # each binding is a dictionary. Let us just print the results
    print "%s: %s (of type %s)" % ("s",binding[u"subj"].value,binding[u"subj"].type)
    print "%s: %s (of type %s)" % ("p",binding[u"prop"].value,binding[u"prop"].type)
    print "%s: %s (of type %s)" % ("o",binding[u"o"].value,binding[u"o"].type)
#'''
'''

queryString = 'PREFIX dc: <http://purl.org/dc/elements/1.1/> INSERT DATA { <http://example/book3> dc:title    "A new book" ; dc:creator  "A.N.Other" . }'
sparql = SPARQLWrapper("http://localhost:8080/openrdf-workbench/repositories/mashtrial/update")

sparql.setQuery(queryString)
sparql.method = 'POST'
sparql.query()
'''
