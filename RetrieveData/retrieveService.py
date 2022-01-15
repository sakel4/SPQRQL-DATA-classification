from .retrieve import retrieve


class retrieveService:

    defaultGraphs = [
        "http://localhost:8890/BNF",
        "http://localhost:8890/DBpedia",
        "http://localhost:8890/Conference",
        "http://localhost:8890/HistMunic",
    ]

    def __init__(self):
        self.retrieveData = retrieve()

    #region #generic
    def getAllTriplets(self,domain):
        print(self.defaultGraphs[domain.value])
        self.retrieveData.setGraph(self.defaultGraphs[domain.value])
        response = self.retrieveData.getAll()
        return response

    def getTypes(self,domain):
        print(self.defaultGraphs[domain.value])
        self.retrieveData.setGraph(self.defaultGraphs[domain.value])
        response = self.retrieveData.getTypes()
        return response
    
    def getPredicates(self,domain):
        print(self.defaultGraphs[domain.value])
        self.retrieveData.setGraph(self.defaultGraphs[domain.value])
        response = self.retrieveData.getAllPredicates()
        return response
    #endregion