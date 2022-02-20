from SPARQLWrapper import SPARQLWrapper, JSON
import json


class Retrieve:

    domain = "http://83.212.77.24:8890/sparql/"
    # constructor
    def __init__(self):
        try:
            self.sparql = SPARQLWrapper(self.domain)
        except:
            print("failed to initialize connection with sparql virtuoso")
        self.sparql.setReturnFormat(JSON)

    # functions
    def setGraph(self, graphURl):
        self.sparql.clearParameter("default-graph-uri")
        self.sparql.addParameter("default-graph-uri", graphURl)

    def getAll(self):
        offset = 0
        response = []
        while True:
            self.sparql.setQuery(
                """
            SELECT ?subject ?predicate ?object
            WHERE { ?subject ?predicate ?object } offset """
                + str(offset)
                + """LIMIT 10000"""
            )
            results = self.sparql.query().convert()
            # print(offset)
            response.extend(results["results"]["bindings"])
            if (len(results["results"]["bindings"])) == 0:
                break
            else:
                print(
                    "offset: "
                    + str(offset)
                    + " length: "
                    + str(len(results["results"]["bindings"]))
                )
                offset = offset + (len(results["results"]["bindings"]))

        jsonResponse = {"instances": response, "size": len(response)}
        return json.dumps(jsonResponse)

    def getTypes(self):
        self.sparql.setQuery(
            """
        select DISTINCT ?object where {
            ?subject rdf:type ?object
        } 
        """
        )
        results = self.sparql.query().convert()
        jsonResponse = {
            "instances": results["results"]["bindings"],
            "size": len(results["results"]["bindings"]),
        }
        return json.dumps(jsonResponse)

    def getAllPredicates(self):
        self.sparql.setQuery(
            """
        select DISTINCT ?predicate where {
            ?subject ?predicate ?object
        } 
        """
        )
        results = self.sparql.query().convert()
        for index in range(len(results["results"]["bindings"])):
            if (
                results["results"]["bindings"][index]["predicate"]["value"]
                == "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"
            ):
                results["results"]["bindings"].pop(index)
                break

        jsonResponse = {
            "instances": results["results"]["bindings"],
            "size": len(results["results"]["bindings"]),
        }
        return json.dumps(jsonResponse)

    def getAllSubjects(self):
        offset = 0
        response = []
        while True:
            self.sparql.setQuery(
                """
            select DISTINCT ?subject where {
                ?subject ?predicate ?object
            }  offset """
                + str(offset)
                + """LIMIT 10000"""
            )
            results = self.sparql.query().convert()
            # print(offset)
            response.extend(results["results"]["bindings"])
            if (len(results["results"]["bindings"])) == 0:
                break
            else:
                offset = offset + (len(results["results"]["bindings"]))

        jsonResponse = {"instances": response, "size": len(response)}
        return json.dumps(jsonResponse)

    def getSubjectType(self, subject):
        self.sparql.setQuery(
            """
        select ?subject ?predicate ?object where {
        ?subject ?predicate ?object .
        ?subject rdf:type ?object .
        FILTER ( ?subject = <"""
            + subject
            + """>)}"""
        )
        results = self.sparql.query().convert()
        jsonResponse = {
            "instances": results["results"]["bindings"],
            "size": len(results["results"]["bindings"]),
        }
        return json.dumps(jsonResponse)
