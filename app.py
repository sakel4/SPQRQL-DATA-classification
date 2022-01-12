from flask import Flask

# from .RetrieveData import RetrieveService

app = Flask(__name__)


# def __init__(self):
#     self.retrieveService = RetrieveService()


@app.route("/BNFtriplets")
def getAllBNFTriplets(self):
    return "test"


# def
