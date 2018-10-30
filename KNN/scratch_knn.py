# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 03:08:49 2018

@author: Student
"""
from sklearn.cross_validation import train_test_split
import unicodecsv
import random
import operator
import math

def getdata(filename):
    with open(filename,'rb') as f:
        reader = unicodecsv.reader(f)
        return list(reader)

def shuffle(i_data):
    random.shuffle(i_data)
    train_data = i_data[:int(0.7*30)]
    test_data = i_data[int(0.7*30):]
    return train_data, test_data
    

def euclideanDist(x, xi):
    d = 0.0
    for i in range(len(x)-1):
        d += pow((float(x[i])-float(xi[i])),2)  #euclidean distance
    d = math.sqrt(d)
    return d

def knn_predict(test_data, train_data, k_value):
    for i in test_data:
        eu_Distance =[]
        knn = []
        v=[0,0,0,0]
        for j in train_data:
            eu_dist = euclideanDist(i, j)
            eu_Distance.append((j[7], eu_dist))
            eu_Distance.sort(key = operator.itemgetter(1))
            knn = eu_Distance[:k_value]
            for k in knn:
                if k[0] ==1:
                    v[0] += 1 
                elif k[0]==2:
                    v[1] +=1
                elif k[0]==3:
                    v[2] +=1
                else:
                    v[3]+=1
            max1=-1
            
            for i in v:
                if v[i]>max1:
                    max1=v[i]
                    maxIndex=i
                    
            i.append(maxIndex)
            
def accuracy(test_data):
    correct = 0
    for i in test_data:
        if i[7] == i[8]:
            correct += 1
    accuracy = float(correct)/len(test_data) *100  #accuracy 
    return accuracy            
    
def main():
    dataset = getdata('out.csv')  #getdata function call with csv file as parameter
    train_dataset, test_dataset = shuffle(dataset) #train test data split
    K = 5              
    for k in range(1,10):                        
        knn_predict(test_dataset, train_dataset, k)   
        print(test_dataset)
        print ("Accuracy : ",accuracy(test_dataset))
        print("\n")
    
if __name__=="__main__":
    main()        
    
    
    
    