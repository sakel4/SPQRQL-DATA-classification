from flask import Flask
# from RetrieveData.Retrieve import retrieve
# from .RetrieveData import RetrieveService

app = Flask(__name__)

# def __init__(self):
#     self.retrieveData = retrieve();
    
@app.route("/BNFtriplets")
def getAllBNFTriplets():
    return "test"


# def
