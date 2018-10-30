# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 03:37:57 2018

@author: Student
"""

class DataPoint:
    def __init__(self, features, label = None):
        self.features = features
        self.label = label
        self.match = 0

    def __iter__(self):
        for f in self.features:
            yield f

        yield self.label

def weight(d_j):
    return 1 / d_j

def distance(x_i, x_j):
    return sum([(x_i.features[i] - x_j.features[i]) ** 2 for i in range(len(x_i.features))]) ** 1 / 2 

def knn(k, x_i, dataPoints):
    knearest = []

    for x_j in dataPoints:
        d_j = distance(x_i, x_j)
        wd_j = weight(d_j)
        x_j.match = wd_j

        if len(knearest) < k:
            knearest.append(x_j)
        elif wd_j > knearest[0].match:
            knearest[0] = x_j
            knearest.sort(key = lambda x: x.match)   

    labels = {}
    nearest = (None, 0)
    for neighbor in knearest:
        if neighbor.label in labels: labels[neighbor] += neighbor.match
        else: labels[neighbor] = neighbor.match

        if labels[neighbor] > nearest[1]:
            nearest = (neighbor, labels[neighbor])
    
    return nearest[0].label