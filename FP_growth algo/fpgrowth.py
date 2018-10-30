# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 01:28:46 2018

@author: Student
"""

import pyfpgrowth

import csv

with open('transactions.csv') as csvfile:
    rows = csv.reader(csvfile)
    res = list(zip(*rows))
   # print(res)
    
patterns = pyfpgrowth.find_frequent_patterns(res, 3)
rules = pyfpgrowth.generate_association_rules(patterns, 0.9)

print(rules)