# svm alogrithm
from sklearn.svm import SVC
# similarity algorithms
# from sklearn.metrics.pairwise import cosine_distances
# from sklearn.metrics.pairwise import euclidean_distances
# from sklearn.metrics.pairwise import manhattan_distances
# from sklearn.metrics import pairwise_distances #default algorithm euclidean

# sklearn functions(score,train datset,data scaling,  confusion matrix and results report)
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

# mathematic python library
import numpy as np
# library for csv files and json
import pandas as pd
import json
#retrieve service class
from RetrieveData.RetrieveService import RetrieveService
from RetrieveData.DomainsEnum import Domains

class MachineLearning:

    type="http://www.w3.org/1999/02/22-rdf-syntax-ns#type"

    def __init__(self):
        self.retrieveService = RetrieveService()
        #for ml algorithm training and testing 
        self.defaultTripletsWithType = [] #default triplets with type [[{x,y,z},{x,y,z},{x,y,z}]
        self.subjectFeaturesWithType = [] #array with subjects features [[0,1,0],[1,0,0],[0,1,1]]
        self.subjectTypes = [] # subjects type [0,4,6]
        #for ml algorithm data classification 
        self.defaultTripletsWithoutType = [] #default triplets without type [[{x,y,z},{x,y,z},{x,y,z}]
        self.subjectsFeaturesWithoutType = [] #array with subjects features (No type) [[0,1,0],[1,0,0],[0,1,1]]

    #removes type predicate 
    def removeTypePredicate(self,predicates): 
        for predicate in predicates:
            if(predicate["predicate"]["value"]=="http://www.w3.org/1999/02/22-rdf-syntax-ns#type"):
                print("true")
                print(predicates.index(predicate))
                predicates.pop(predicates.index(predicate))
                break;
        return predicates

    #get type index value
    def getTypeIndex(self,typeValue):
        for currentType in self.types:
            if(currentType["object"]["value"]==typeValue):
                return self.types.index(currentType)
        return -1 #missing type

    # get predicate index value
    def getPredicateIndex(self,predicateValue):
        for currentPredicate in self.predicates:
            if(currentPredicate["predicate"]["value"]==predicateValue):
                return self.predicates.index(currentPredicate)
        return -1 #missing type

    #gets data and convert them to arrays ready for ml algorithm classification
    def getAndConvertToArray(self):
        #api requests
        self.types = json.loads(self.retrieveService.getTypes(Domains.DB_PEDIA))["instances"] #types
        self.predicates = self.removeTypePredicate(json.loads(self.retrieveService.getPredicates(Domains.DB_PEDIA))["instances"]) #predicates
        self.subjects = json.loads(self.retrieveService.getSubjects(Domains.DB_PEDIA))["instances"] #subjects
        triplets = json.loads(self.retrieveService.getAllTriplets(Domains.DB_PEDIA))["instances"] #all triplets

        for subject in self.subjects:
            hasType = False # False means no type, True means type available
            currentSubjectDefaultTriplets = []
            currentSubjectFeatures = [0] * len(self.predicates) # array with size equal with the number of the available predicates
            currentSubjectType = -1 #negative value means no type, every number equal or greater than 0 signifies the subject type

            for triplet in triplets:
                if(triplet["subject"]["value"] == subject["subject"]["value"]):
                    if(triplet["predicate"]["value"]==self.type):
                        hasType=True;
                        currentSubjectType = self.getTypeIndex(triplet["object"]["value"])
                    else:
                        currentSubjectFeatures[self.getPredicateIndex(triplet["predicate"]["value"])] = 1 
                    currentSubjectDefaultTriplets.append(triplet)
            if(hasType==True):
                self.defaultTripletsWithType.append(currentSubjectDefaultTriplets)
                self.subjectFeaturesWithType.append(currentSubjectFeatures)
                self.subjectTypes.append(currentSubjectType)
            else:
                self.defaultTripletsWithoutType.append(currentSubjectDefaultTriplets)
                self.subjectsFeaturesWithoutType.append(currentSubjectFeatures)
            
        #find the bug
        # for triplet in triplets:
        #     #same subject
        #     if(triplet["subject"]["value"]==currentSubject):
        #         # print("has")
        #         if(triplet["predicate"]["value"]==self.type):
        #             hasType=True;
        #             currentSubjectType = self.getTypeIndex(triplet["object"]["value"])
                # currentSubjectDefaultTriplets.append(triplet)
                # currentSubjectFeatures[self.getPredicateIndex(triplet["predicate"]["value"])] = 1 
        #     #new subject
        #     else:
        #         # print("hasn't")
                # if(hasType==True):
                #     self.defaultTripletsWithType.append(currentSubjectDefaultTriplets)
                #     self.subjectFeaturesWithType.append(currentSubjectFeatures)
                #     self.subjectTypes.append(currentSubjectType)
                # else:
                #     self.defaultTripletsWithoutType.append(currentSubjectDefaultTriplets)
                #     self.subjectsFeaturesWithoutType.append(currentSubjectFeatures)
        #         hasType=False
        #         currentSubjectDefaultTriplets =[]
        #         currentSubjectFeatures = [0] * len(self.predicates)
        #         currentSubjectType = -1
        #         currentSubject = triplet["subject"]["value"]
        #         if(triplet["predicate"]["value"]==type):
        #             hasType=True;
        #             currentSubjectType = self.getTypeIndex(triplet["object"]["value"])
        #         currentSubjectDefaultTriplets.append(triplet)
        #         currentSubjectFeatures[self.getPredicateIndex(triplet["predicate"]["value"])] = 1 


        
        print(len(self.defaultTripletsWithType))
        print(len(self.subjectFeaturesWithType))
        print(len(self.subjectTypes))
        # print(len(self.subjects))
        print("____________________________________")
        print(len(self.defaultTripletsWithoutType))
        print(len(self.subjectsFeaturesWithoutType))
        return self.predicates

    def classify():
        # import data
        dataset = pd.read_csv('Social_Network_Ads.csv')
        X = dataset.iloc[:, :-1].values
        y = dataset.iloc[:, -1].values
    
        # spliting data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)
    
        # feature scaling
        sc = StandardScaler()
        X_train = sc.fit_transform(X_train)
        X_test = sc.transform(X_test)
    
        # train
        classifier = SVC(kernel = "rbf", random_state = 0) #SVC machine learning algorithm
        # classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski') #KNN machine learning algorithm
        classifier.fit(X_train, y_train)
    
        #prediction
        y_pred = classifier.predict(X_test)
        # print(classifier.predict_proba(X_test))
        # print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))
    
        # print confusion matrix, accuracy  score and results report
        cm = confusion_matrix(y_test, y_pred)
        print(cm)
        print(accuracy_score(y_test, y_pred))
        print(classification_report(y_test, y_pred))