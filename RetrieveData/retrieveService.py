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
    
    #region #BNF
    def getAllBNF(self):
        self.retrieveData.setGraph(self.defaultGraphs[0])
        response = self.retrieveData.getAll()
        return response

    def getBNFtypes(self):
        self.retrieveData.setGraph(self.defaultGraphs[0])
        response = self.retrieveData.getTypes()
        return response
    
    def getBNFpredicates(self):
        self.retrieveData.setGraph(self.defaultGraphs[0])
        response = self.retrieveData.getAllPredicates()
        return response
    #endregion

    #region #DBpedia
    def getAllDBPedia(self):
        self.retrieveData.setGraph(self.defaultGraphs[1])
        response = self.retrieveData.getAll()
        return response
    
    def getDBPediaTypes(self):
        self.retrieveData.setGraph(self.defaultGraphs[1])
        response = self.retrieveData.getTypes()
        return response
    
    def getDBPediaPredicates(self):
        self.retrieveData.setGraph(self.defaultGraphs[1])
        response = self.retrieveData.getAllPredicates()
        return response
    #endregion

    #region #Conference
    def getAllConference(self):
        self.retrieveData.setGraph(self.defaultGraphs[2])
        response = self.retrieveData.getAll()
        return response

    def getConferenceTypes(self):
        self.retrieveData.setGraph(self.defaultGraphs[2])
        response = self.retrieveData.getTypes()
        return response
    
    def getConferencePredicates(self):
        self.retrieveData.setGraph(self.defaultGraphs[2])
        response = self.retrieveData.getAllPredicates()
        return response
    #endregion
    
    #region #HustMunic
    def getAllHistMunic(self):
        self.retrieveData.setGraph(self.defaultGraphs[3])
        response = self.retrieveData.getAll()
        return response

    def getHistMunicTypes(self):
        self.retrieveData.setGraph(self.defaultGraphs[3])
        response = self.retrieveData.getTypes()
        return response
    
    def getHistMunicPredicates(self):
        self.retrieveData.setGraph(self.defaultGraphs[3])
        response = self.retrieveData.getAllPredicates()
        return response
    #endregion