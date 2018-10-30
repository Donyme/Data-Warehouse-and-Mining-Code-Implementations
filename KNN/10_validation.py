# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 02:07:12 2018

@author:Dibyanshu 
"""

from sklearn import model_selection

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

 
def importdata():
    balance_data = pd.read_csv('out.csv',sep= ',')
     

    print ("Dataset Length: ", len(balance_data))
    print ("Dataset Shape: ", balance_data.shape)

    print ("Dataset: ",balance_data.head())
    return balance_data
 

def splitdataset(balance_data):
 

    X = balance_data.values[1:, 1:7]
    Y = balance_data.values[1:, 7]
 

    X_train, X_test, y_train, y_test = train_test_split( 
    X, Y, test_size = 0.3, random_state = 100)
     
    return X, Y, X_train, X_test, y_train, y_test
    
    
def main():
    data = importdata()
    X, Y, X_train, X_test, y_train, y_test = splitdataset(data)
    #Neighbors
    neighbors = filter(lambda x: x % 2 != -1 , list(range(1,50)))
     
    #Create empty list that will hold cv scores
    cv_scores = []
     
    #Perform 10-fold cross validation on training set for odd values of k:
    seed=123
    for k in neighbors:
        k_value = k+1
        knn = KNeighborsClassifier(n_neighbors = k_value, weights='uniform', p=2, metric='euclidean')
        kfold = model_selection.KFold(n_splits=10, random_state=seed)
        scores = model_selection.cross_val_score(knn, X_train, y_train, cv=kfold, scoring='accuracy')
        cv_scores.append(scores.mean()*100)
        print("k=%d %0.2f (+/- %0.2f)" % (k_value, scores.mean()*100, scores.std()*100))
     
    optimal_k = neighbors[cv_scores.index(max(cv_scores))]
    print "The optimal number of neighbors is %d with %0.1f%%" % (optimal_k, cv_scores[optimal_k])
     
    plt.plot(neighbors, cv_scores)
    plt.xlabel('Number of Neighbors K')
    plt.ylabel('Train Accuracy')
    plt.show()
 
if __name__=="__main__":
    main()    