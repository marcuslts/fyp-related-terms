from SPARQLWrapper import SPARQLWrapper, JSON

class Query:

    def get_abstract(self):
        sparql = SPARQLWrapper('https://dbpedia.org/sparql')
        sparql_query = f'''SELECT ?object WHERE {{ dbr:{self.input} dbo:abstract ?object .}} '''
        sparql.setQuery(sparql_query)
        sparql.setReturnFormat(JSON)
        result = sparql.query().convert()
        abstract = ""
        for res in result['results']['bindings']:
            lang, value = res['object']['xml:lang'], res['object']['value']
            if lang == 'en':
                abstract = value
        return abstract

    def get_links(self):
        sparql = SPARQLWrapper('https://dbpedia.org/sparql')
        sparql_query = f'''SELECT ?object WHERE {{ dbr:{self.input} dbo:wikiPageWikiLink ?object .}} '''
        sparql.setQuery(sparql_query)
        sparql.setReturnFormat(JSON)
        result = sparql.query().convert()
        links = []
        for res in result['results']['bindings']:
            # Get related word or phrase
            value = res['object']['value']
            # Remove url link "http://dbpedia.org/resource/" from value
            value = value.lstrip("http://dbpedia.org/resource/")
            # Remove categories as they do not contain abstracts
            if value.find("Category:") == -1:
                if value.find("(") == -1:
                    links.append(value)
        return links

    def __init__(self, input):
        self.input = input 