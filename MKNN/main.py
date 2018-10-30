# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 03:38:54 2018

@author: Student
"""

import matplotlib.pyplot as plt
import random
import mknn as knn
from sklearn.cross_validation import train_test_split

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
    
random.seed(200)

points = []
for i in range(700):  
    x = random.uniform(0, 10)
    y = random.uniform(0, 10)

    label = "#177ACC"
    if x < 4 and y >= 3: label = "#E8B542"
    if x >= 4 and y >= 3: label = "#BF0001"
    if x >= 4 and y < 3: label = "#04CA95"

    points.append(knn.DataPoint([x, y], label))

x, y, l = zip(*points)
plt.scatter(x, y, color=l)

pred = []
for i in range(300):  
    x = random.uniform(0, 10)
    y = random.uniform(0, 10)
    pred.append(knn.DataPoint([x, y]))

for p in pred:
    p.label = knn.knn(5, p, points)

x, y, l = zip(*pred)
plt.scatter(x, y, color=l, s = 100, marker = "D")

plt.show()