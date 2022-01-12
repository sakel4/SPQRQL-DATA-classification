from SPARQLWrapper import SPARQLWrapper, JSON


class Retrieve:

    domain = "http://83.212.77.24:8890/sparql/"

    def __init__(self):
        try:
            self.sparql = SPARQLWrapper(self.domain)
        except:
            print("failed to initialize connection with sparql virtuoso")
        self.sparql.setReturnFormat(JSON)

    def setGraph(self, graphURl):
        self.sparql.addParameter("default-graph-uri", graphURl)

    def getAll(self):
        offset = 0
        response = []
        while True:
            self.sparql.setQuery(
                """
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            SELECT ?x ?y ?z
            WHERE { ?x ?y ?z }"""
                + str(offset)
                + """LIMIT 10000"""
            )
            results = self.sparql.query().convert()
            response.extend(results["results"]["bindings"])
            if len(results["results"]["bindings"]) == 0:
                break
            elif offset == 0:
                offset = offset + len(results["results"]["bindings"])

        return response

    def getTypes(self):
        self.sparql.setQuery(
            """
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        select DISTINCT ?z where {
            ?x rdf:type ?z
        } 
        """
        )
        results = self.sparql.query().convert()
        return results["results"]["bindings"]

    def getAllPredicates(self):
        self.sparql.setQuery(
            """
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        select DISTINCT ?y where {
            ?x ?y ?z
        } 
        """
        )
        results = self.sparql.query().convert()
        return results["results"]["bindings"]
