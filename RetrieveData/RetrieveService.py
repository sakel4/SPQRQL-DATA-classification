from .Retrieve import Retrieve


class RetrieveService:

    defaultGraphs = [
        "http://localhost:8890/BNF",
        "http://localhost:8890/DBpedia",
        "http://localhost:8890/Conference",
        "http://localhost:8890/HistMunic",
    ]

    def __init__(self):
        self.retrieveData = Retrieve()

    # region #generic
    def getAllTriplets(self, domain):
        self.retrieveData.setGraph(self.defaultGraphs[domain.value])
        response = self.retrieveData.getAll()
        return response

    def getTypes(self, domain):
        self.retrieveData.setGraph(self.defaultGraphs[domain.value])
        response = self.retrieveData.getTypes()
        return response

    def getPredicates(self, domain):
        self.retrieveData.setGraph(self.defaultGraphs[domain.value])
        response = self.retrieveData.getAllPredicates()
        return response

    def getSubjects(self, domain):
        self.retrieveData.setGraph(self.defaultGraphs[domain.value])
        response = self.retrieveData.getAllSubjects()
        return response

    def getSubjectType(self, domain, subject):
        self.retrieveData.setGraph(self.defaultGraphs[domain.value])
        response = self.retrieveData.getSubjectType(subject)
        return response

    # endregion
