# svm alogrithm
from sklearn.svm import SVC

# sklearn functions(score,train datset,data scaling,  confusion matrix and results report)
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# from sklearn.metrics.precision_score import precision_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

# mathematic python library
import numpy as np

# library for csv files and json
import json
import time

# retrieve service class
from RetrieveData.RetrieveService import RetrieveService
from RetrieveData.DomainsEnum import Domains


class MachineLearning:

    type = "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"

    def __init__(self):
        self.retrieveService = RetrieveService()
        # -->for ml algorithm training and testing
        # default triplets with type [[{x,y,z},{x,y,z},{x,y,z}],[...],[...]]
        self.defaultTripletsWithType = []
        # array with subjects features [[0,1,0],[1,0,0],[0,1,1]]
        self.subjectFeaturesWithType = []
        self.subjectTypes = []  # subjects type [0,4,6]
        # -->for ml algorithm data classification
        # default triplets without type [[{x,y,z},{x,y,z},{x,y,z}]
        self.defaultTripletsWithoutType = []
        # array with subjects features (No type) [[0,1,0],[1,0,0],[0,1,1]]
        self.subjectsFeaturesWithoutType = []

    # removes type predicate
    def removeTypePredicate(self, predicates):
        for predicate in predicates:
            if (
                predicate["predicate"]["value"]
                == "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"
            ):
                predicates.pop(predicates.index(predicate))
                break
        return predicates

    # get type index value
    def getTypeIndex(self, typeValue):
        for currentType in self.types:
            if currentType["object"]["value"] == typeValue:
                return self.types.index(currentType)
        return -1  # missing type

    # get predicate index value
    def getPredicateIndex(self, predicateValue):
        for currentPredicate in self.predicates:
            if currentPredicate["predicate"]["value"] == predicateValue:
                return self.predicates.index(currentPredicate)
        return -1  # missing type

    # gets data and convert them to arrays ready for ml algorithm classification
    def getAndConvertToArray(self, dataset):
        self.dataset = dataset
        self.defaultTripletsWithType = []
        self.subjectFeaturesWithType = []
        self.subjectTypes = []
        self.defaultTripletsWithoutType = []
        self.subjectsFeaturesWithoutType = []

        # api requests
        # types
        self.types = json.loads(self.retrieveService.getTypes(dataset))["instances"]
        # subjects
        self.subjects = json.loads(self.retrieveService.getSubjects(dataset))[
            "instances"
        ]
        # predicates
        self.predicates = self.removeTypePredicate(
            json.loads(self.retrieveService.getPredicates(dataset))["instances"]
        )
        # all triplets
        triplets = json.loads(self.retrieveService.getAllTriplets(dataset))["instances"]
        triplets.sort(key=lambda x: x["subject"]["value"], reverse=False)

        hasType = False  # False means no type, True means type available
        currentSubject = triplets[0]["subject"]["value"]
        currentSubjectDefaultTriplets = []
        # array with size equal with the number of the available predicates
        currentSubjectFeatures = [0] * len(self.predicates)
        # negative value means no type, every number equal or greater than 0 signifies the subject type
        currentSubjectType = -1
        cnt = 1
        # not that proud (needs some thought)
        for triplet in triplets:
            # check if the subject is the same with the current
            if triplet["subject"]["value"] != currentSubject:
                cnt = cnt + 1
                currentSubject = triplet["subject"]["value"]
                if hasType == True:
                    self.defaultTripletsWithType.append(currentSubjectDefaultTriplets)
                    self.subjectFeaturesWithType.append(currentSubjectFeatures)
                    self.subjectTypes.append(currentSubjectType)
                else:
                    self.defaultTripletsWithoutType.append(
                        currentSubjectDefaultTriplets
                    )
                    self.subjectsFeaturesWithoutType.append(currentSubjectFeatures)
                hasType = False
                currentSubjectDefaultTriplets = []
                currentSubjectFeatures = [0] * len(self.predicates)

            currentSubjectDefaultTriplets.append(triplet)

            if triplet["predicate"]["value"] == self.type:
                hasType = True
                currentSubjectType = self.getTypeIndex(triplet["object"]["value"])

            predicateIndex = self.getPredicateIndex(triplet["predicate"]["value"])
            if predicateIndex != -1:
                currentSubjectFeatures[predicateIndex] = 1

            if triplet == triplets[(len(triplets) - 1)]:
                if hasType == True:
                    self.defaultTripletsWithType.append(currentSubjectDefaultTriplets)
                    self.subjectFeaturesWithType.append(currentSubjectFeatures)
                    self.subjectTypes.append(currentSubjectType)
                else:
                    self.defaultTripletsWithoutType.append(
                        currentSubjectDefaultTriplets
                    )
                    self.subjectsFeaturesWithoutType.append(currentSubjectFeatures)

    def classify(self, dataset, statistics):
        self.getAndConvertToArray(dataset)
        self.startTime = time.time()

        # spliting data
        X_train, X_test, y_train, y_test = train_test_split(
            self.subjectFeaturesWithType,
            self.subjectTypes,
            test_size=0.30,
            random_state=2,
        )

        # feature scaling
        sc = StandardScaler()
        X_train = sc.fit_transform(X_train)
        X_test = sc.transform(X_test)
        # SVC machine learning algorithm
        classifier = SVC(kernel="rbf", random_state=0)
        classifier.fit(X_train, y_train)
        # prediction
        y_pred = np.array(classifier.predict(X_test))
        y_test = np.array(y_test)

        FeaturesForPrediction = []
        newPredictions = []
        if len(self.subjectsFeaturesWithoutType):
            # subjcts feature matrix without types
            FeaturesForPrediction = sc.transform(self.subjectsFeaturesWithoutType)
            newPredictions = classifier.predict(FeaturesForPrediction)

        self.finishTime = time.time()

        # merge known with predicted
        self.subjectFeaturesWithType.extend(self.subjectsFeaturesWithoutType)
        self.subjectTypes.extend(newPredictions)
        self.defaultTripletsWithType.extend(self.defaultTripletsWithoutType)

        if statistics:
            return self.generateStatistics(
                y_test, y_pred, self.generateTypePatternsStatistics()
            )
        else:
            return json.dumps(
                {
                    "subjectsTriplets": np.array(self.defaultTripletsWithType).tolist(),
                    "subjectsTypes": self.convertToTypeTriplet(self.subjectTypes),
                }
            )

    def convertToTypeTriplet(self, typesList):
        returnTypes = []
        for type in typesList:
            returnTypes.append(self.types[type])

        return returnTypes

    def generateStatistics(
        self, testFeaturesMatrix, predictionsTargetVectorMatrix, typeStatistics
    ):
        cm = confusion_matrix(testFeaturesMatrix, predictionsTargetVectorMatrix)

        FP = cm.sum(axis=0) - np.diag(cm)
        FN = cm.sum(axis=1) - np.diag(cm)
        TP = np.diag(cm)
        TN = cm.sum() - (FP + FN + TP)
        FP = FP.astype(float)
        FN = FN.astype(float)
        TP = TP.astype(float)
        TN = TN.astype(float)
        # Sensitivity, hit rate, recall, or true positive rate
        TPR = TP / (TP + FN)
        # Fall out or false positive rate
        FPR = FP / (FP + TN)

        TPRsum = sum(TPR.tolist())
        FPRsum = sum(FPR.tolist())

        # print(precision_score(y_test, y_pred))

        return json.dumps(
            {
                "algorithm": "SVM",
                "dataset": self.dataset.name,
                "types": typeStatistics,
                "statistics": {
                    "executionTime": (self.finishTime - self.startTime) * 1000,
                    "precision": precision_score(
                        testFeaturesMatrix,
                        predictionsTargetVectorMatrix,
                        average="weighted",
                    ),
                    "recall": recall_score(
                        testFeaturesMatrix,
                        predictionsTargetVectorMatrix,
                        average="weighted",
                    ),
                    "fMeasure": f1_score(
                        testFeaturesMatrix,
                        predictionsTargetVectorMatrix,
                        average="weighted",
                    ),
                    "truePositivePercentage": TPRsum / len(TPR),
                    "falsePositivePercentage": FPRsum / len(TPR),
                },
            }
        )

    def generateTypePatternsStatistics(self):
        typesStats = []
        for index in range(len(self.types)):
            instances = self.subjectTypes.count(index)
            relations = []
            relations = self.generateRelations(self.types[index]["object"]["value"])
            typesStats.append(
                {
                    "type_id": self.types[index]["object"]["value"],
                    "typeName": self.types[index]["object"]["value"].split("/")[-1],
                    "instancesFound": instances,
                    "patterns": self.findTypesPatterns(index),
                    # "tt": self.predicates,
                    "relations": relations,
                    "fiveExampleInstances": self.getFiveInstances(instances, index),
                }
            )

        return typesStats

    def generateRelations(self, currentType):
        print("Type: " + currentType)
        relations = []
        for index in range(len(self.subjectTypes)):
            if currentType == self.types[self.subjectTypes[index]]["object"]["value"]:
                for subjectTriplet in self.defaultTripletsWithType[index]:
                    type = self.findIfItIsSubject(subjectTriplet["object"]["value"])
                    if type != None:
                        if (
                            self.checkIfRelationExists(
                                relations, subjectTriplet["predicate"]["value"], type
                            )
                            == False
                        ):
                            relations.append(
                                {
                                    "propertyName": subjectTriplet["predicate"][
                                        "value"
                                    ],
                                    "relatedTypeId": type,
                                    "relatedInstances": 1,
                                }
                            )
        return relations

    def checkIfRelationExists(self, relations, property, relatedType):
        for relation in relations:
            if (
                relation["propertyName"] == property
                and relation["relatedTypeId"] == relatedType
            ):
                relation["relatedInstances"] = relation["relatedInstances"] + 1
                return True
        return False

    def findIfItIsSubject(self, object):
        type = None
        for subject in self.subjects:
            # print()
            if subject["subject"]["value"] == object:
                for index in range(len(self.defaultTripletsWithType)):
                    triplets = self.defaultTripletsWithType[index]
                    if triplets[0]["subject"]["value"] == object:
                        for triplet in triplets:
                            if triplet["predicate"]["value"] == self.type:
                                type = triplet["object"]["value"]
                                break
                        if type != None:
                            break
                if type != None:
                    break

        return type

    def findTypesPatterns(self, typeIndex):
        typesPatterns = []
        for index in range(len(self.subjectTypes)):
            if self.subjectTypes[index] == typeIndex:
                triplets = self.defaultTripletsWithType[index]
                pattern = []
                for triplet in triplets:
                    if triplet["predicate"]["value"] != self.type:
                        pattern.append(triplet["predicate"]["value"])
                if len(pattern) > 0:
                    if typesPatterns.count(pattern) == 0:
                        typesPatterns.append(pattern)

        return typesPatterns

    def getFiveInstances(self, numberOfInstances, typeIndex):
        returnInstances = 0
        if numberOfInstances > 5:
            returnInstances = 5
        else:
            returnInstances = numberOfInstances
        instances = []
        for index in range(len(self.subjectTypes)):
            if self.subjectTypes[index] == typeIndex:
                triplets = self.defaultTripletsWithType[index]
                instances.append(triplets[0]["subject"]["value"])
                if len(instances) == returnInstances:
                    break

        return instances
