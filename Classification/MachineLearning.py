# svm alogrithm
from sklearn.svm import SVC
# knn algorithm
# from sklearn.neighbors import KNeighborsClassifier
# similarity algorithms
from sklearn.metrics.pairwise import cosine_distances
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.metrics.pairwise import manhattan_distances
from sklearn.metrics import pairwise_distances #default algorithm euclidean

# sklearn functions(score,train datset,data scaling,  confusion matrix and results report)
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

# mathematic python library
import numpy as np
# library for csv files
import pandas as pd

class MachineLearning:
# import data

    def classify():
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