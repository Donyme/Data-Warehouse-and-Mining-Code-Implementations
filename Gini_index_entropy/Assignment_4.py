# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 14:50:47 2018

@author: Student
"""

import pandas as pd
 
# creating file handler for 
# our example.csv file in
# read mode
file_handler = open("cardata.csv", "r")
 
# creating a Pandas DataFrame
# using read_csv function 
# that reads from a csv file.
data = pd.read_csv(file_handler, sep = ",")

# closing the file handler
file_handler.close()
 
# creating a dict file 
buying = {'vhigh': 1,'high': 2,'med':3,'low':4}
maint = {'vhigh': 1,'high': 2,'med':3,'low':4}
doors = {'2':1,'3':2,'4':3,'5more':4}
persons = {'2':1,'4':2,'more':3}
lugboot = {'small': 1,'med':2,'big':3}
safety = {'high': 1,'med':2,'low':3}
acceptability = {'unacc': 1,'acc':2,'good':3,'vgood':4}

 
# traversing through dataframe
# Gender column and writing
# values where key matches
print data.iloc[1:, [1]]

data.buying = [buying[item] for item in data.buying]
data.maint = [maint[item] for item in data.maint]
data.doors = [doors[item] for item in data.doors]
data.persons = [persons[item] for item in data.persons]
data.lugboot = [lugboot[item] for item in data.lugboot]
data.safety = [safety[item] for item in data.safety]
data.acceptability = [acceptability[item] for item in data.acceptability]
data.to_csv('out.csv')
print data