  
from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper('https://dbpedia.org/sparql')

def obtener_ingredientes(ingredient):
    sparql.setQuery(f'''
        SELECT ?res
        WHERE {{ 
            dbr:{ingredient} dbo:abstract ?res .
            FILTER (lang(?res) = "es") 
        }}
    ''')
    sparql.setReturnFormat(JSON)
    qres = sparql.query().convert()
    if len(qres['results']['bindings']) == 0:
        return "Información no encontrada"
    else:
        result = qres['results']['bindings'][0]
        ingredient = result['res']['value']
        return ingredient


def obtener_photoIngredientes(ingredient):
    sparql.setQuery(f'''
        SELECT ?image
        WHERE {{ 
            dbr:{ingredient} dbo:abstract ?res .
            dbr:{ingredient} foaf:depiction ?image .
        }}
    ''')
    sparql.setReturnFormat(JSON)
    qres = sparql.query().convert()
    if len(qres['results']['bindings']) == 0:
        return "Imagen no disponible"
    else:
        result = qres['results']['bindings'][0]
        image = result['image']['value']
        return image