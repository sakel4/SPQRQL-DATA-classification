from flask import Flask,request
import json
from RetrieveData.retrieveService import retrieveService
from RetrieveData.DomainsEnum import Domains

app = Flask(__name__)


rt = retrieveService();
    
def checkIfDatasetExist(dataset):
    for domain in Domains:
        if(dataset==domain.name):
            return domain
            break;
    return None;

#region #BNF
@app.route("/triplets")
def getAllBNFTriplets():
    #return 400 status code and error message about missing dataset
    if(request.args.get("dataset")==None):
        return json.dumps({"error": "This dataset is missing"}),400
    #search if dataset exist
    dataset = checkIfDatasetExist(request.args.get("dataset"))
    #return 400 status code and error message about dataset parameter value does not match with our datasets
    if(dataset == None):
        return json.dumps({"error": "This dataset does not exist"}),400
    return rt.getAllTriplets(dataset);

@app.route("/types")
def getAllBNFTypes():
        #return 400 status code and error message about missing dataset
    if(request.args.get("dataset")==None):
        return json.dumps({"error": "This dataset is missing"}),400
    #search if dataset exist
    dataset = checkIfDatasetExist(request.args.get("dataset"))
    #return 400 status code and error message about dataset parameter value does not match with our datasets
    if(dataset == None):
        return json.dumps({"error": "This dataset does not exist"}),400
    return rt.getTypes(dataset);

@app.route("/predicates")
def getAllBNFPredicates():
        #return 400 status code and error message about missing dataset
    if(request.args.get("dataset")==None):
        return json.dumps({"error": "This dataset is missing"}),400
    #search if dataset exist
    dataset = checkIfDatasetExist(request.args.get("dataset"))
    #return 400 status code and error message about dataset parameter value does not match with our datasets
    if(dataset == None):
        return json.dumps({"error": "This dataset does not exist"}),400
    return rt.getPredicates(dataset);
#endregion