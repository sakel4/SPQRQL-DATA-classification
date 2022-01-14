from Retrieve import retrieve


class retrieveService:

    defaultGraphs = [
        "http://localhost:8890/BNF",
        "http://localhost:8890/DBpedia",
        "http://localhost:8890/Conference",
        "http://localhost:8890/HistMunic",
    ]

    def __init__(self):
        self.retrieveData = retrieve()

    def getAllBNF(self):
        self.retrieveData.setGraph(self.defaultGraphs[0])
        response = self.retrive.getAll()
        print(len(response))
