# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 01:37:32 2018

@author: Student
"""

from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering

iris = datasets.load_iris()
X = iris.data

scaler = StandardScaler()
X_std = scaler.fit_transform(X)

clt = AgglomerativeClustering(linkage='ward', 
                              affinity='euclidean', 
                              n_clusters=3)

# Train model
model = clt.fit(X_std)
print(model.labels_)