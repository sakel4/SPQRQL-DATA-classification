from Retrieve import Retrieve


class RetrieveService:

    defaultGraphs = [
        "http://localhost:8890/BNF",
        "http://localhost:8890/DBpedia",
        "http://localhost:8890/Conference",
        "http://localhost:8890/HistMunic",
    ]

    def __init__(self):
        self.retrive = Retrieve()

    def getAllBNF(self):
        self.retrive.setGraph(self.defaultGraphs[0])
        response = self.retrive.getAll()
        print(len(response))
