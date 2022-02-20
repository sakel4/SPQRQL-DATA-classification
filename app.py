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


# @app.route("/subjectTypes", methods=["GET"])
# def getSubjectType():
#     datasetSubject = request.args.get("subject")
#     datasetParam = request.args.get("dataset")
#     dataset = checkIfDatasetExist(datasetParam)
#     return rt.getSubjectType(dataset, datasetSubject)


# region #endpoints
@app.route("/triplets", methods=["GET"])
def getAllTriplets():
    datasetParam = request.args.get("dataset")
    # return 400 status code and error message about missing dataset
    if datasetParam == None:
        return json.dumps({"error": "dataset parameter is missing"}), 400
    # search if dataset exist
    dataset = checkIfDatasetExist(datasetParam)
    # return 400 status code and error message about dataset parameter value does not match with our datasets
    if dataset == None:
        return json.dumps({"error": "This dataset does not exist"}), 400
    return rt.getAllTriplets(dataset)


@app.route("/types", methods=["GET"])
def getAllTypes():
    datasetParam = request.args.get("dataset")
    # return 400 status code and error message about missing dataset
    if datasetParam == None:
        return json.dumps({"error": "dataset parameter is missing"}), 400
    # search if dataset exist
    dataset = checkIfDatasetExist(datasetParam)
    # return 400 status code and error message about dataset parameter value does not match with our datasets
    if dataset == None:
        return json.dumps({"error": "This dataset does not exist"}), 400
    return rt.getTypes(dataset)


@app.route("/predicates", methods=["GET"])
def getAllPredicates():
    datasetParam = request.args.get("dataset")
    # return 400 status code and error message about missing dataset
    if datasetParam == None:
        return json.dumps({"error": "dataset parameter is missing"}), 400
    # search if dataset exist
    dataset = checkIfDatasetExist(datasetParam)
    # return 400 status code and error message about dataset parameter value does not match with our datasets
    if dataset == None:
        return json.dumps({"error": "This dataset does not exist"}), 400
    return rt.getPredicates(dataset)


@app.route("/subjects", methods=["GET"])
def getAllSubjects():
    datasetParam = request.args.get("dataset")
    # return 400 status code and error message about missing dataset
    if datasetParam == None:
        return json.dumps({"error": "dataset parameter is missing"}), 400
    # search if dataset exist
    dataset = checkIfDatasetExist(datasetParam)
    # return 400 status code and error message about dataset parameter value does not match with our datasets
    if dataset == None:
        return json.dumps({"error": "This dataset does not exist"}), 400
    return rt.getSubjects(dataset)


@app.route("/classification", methods=["GET"])
def classifyDataset():
    datasetParam = request.args.get("dataset")
    statisticsParam = request.args.get("statistics")
    # return 400 status code and error message about missing dataset
    if datasetParam == None:
        return json.dumps({"error": "dataset parameter is missing"}), 400
    if statisticsParam == None:
        return json.dumps({"error": "statistics parameter is missing"}), 400
    if statisticsParam != "true" and statisticsParam != "false":
        return (
            json.dumps({"error": "statistics parameter value must be true or false"}),
            400,
        )
    # search if dataset exist
    dataset = checkIfDatasetExist(datasetParam)
    # return 400 status code and error message about dataset parameter value does not match with our datasets
    if dataset == None:
        return json.dumps({"error": "This dataset does not exist"}), 400

    statistics = statisticsParam == "true"
    return ml.classify(dataset, statistics)


# endregion
