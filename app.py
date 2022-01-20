from flask import Flask, request
import json
from RetrieveData.RetrieveService import RetrieveService
from RetrieveData.DomainsEnum import Domains
from Classification.MachineLearning import MachineLearning

app = Flask(__name__)


rt = RetrieveService()
ml = MachineLearning()


def checkIfDatasetExist(dataset):
    for domain in Domains:
        if dataset == domain.name:
            return domain
            break
    return None


# region #endpoints
@app.route("/triplets")
def getAllTriplets():
    # return 400 status code and error message about missing dataset
    if request.args.get("dataset") == None:
        return json.dumps({"error": "This dataset is missing"}), 400
    # search if dataset exist
    dataset = checkIfDatasetExist(request.args.get("dataset"))
    # return 400 status code and error message about dataset parameter value does not match with our datasets
    if dataset == None:
        return json.dumps({"error": "This dataset does not exist"}), 400
    return rt.getAllTriplets(dataset)


@app.route("/types")
def getAllTypes():
    # return 400 status code and error message about missing dataset
    if request.args.get("dataset") == None:
        return json.dumps({"error": "This dataset is missing"}), 400
    # search if dataset exist
    dataset = checkIfDatasetExist(request.args.get("dataset"))
    # return 400 status code and error message about dataset parameter value does not match with our datasets
    if dataset == None:
        return json.dumps({"error": "This dataset does not exist"}), 400
    return rt.getTypes(dataset)


@app.route("/predicates")
def getAllPredicates():
    # return 400 status code and error message about missing dataset
    if request.args.get("dataset") == None:
        return json.dumps({"error": "This dataset is missing"}), 400
    # search if dataset exist
    dataset = checkIfDatasetExist(request.args.get("dataset"))
    # return 400 status code and error message about dataset parameter value does not match with our datasets
    if dataset == None:
        return json.dumps({"error": "This dataset does not exist"}), 400
    return rt.getPredicates(dataset)


@app.route("/convertion")
def convertDataset():
    # return 400 status code and error message about missing dataset
    if request.args.get("dataset") == None:
        return json.dumps({"error": "This dataset is missing"}), 400
    # search if dataset exist
    dataset = checkIfDatasetExist(request.args.get("dataset"))
    # return 400 status code and error message about dataset parameter value does not match with our datasets
    if dataset == None:
        return json.dumps({"error": "This dataset does not exist"}), 400
    return ml.getAndConvertToArray(dataset)
    # return json.dumps(ml.getAndConvertToArray())
    # return "done"


@app.route("/classification")
def classifyDataset():
    return ml.classify()


# endregion
