#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 14:23:23 2017

@author: cuiqy
"""

from sklearn.naive_bayes import GaussianNB
data_table = [[1,1,1,0],
[0,0,0,1],
[0,1,0,0],
[1,0,0,0],
[1,1,0,1],
[1,0,0,1],
[0,1,1,1],
[0,0,0,0],
[1,0,1,0],
[0,1,0,1]]
X=[[1,1],[0,0],[0,1],[1,0],[1,1],[1,0],[0,1],[0,0],[1,0],[0,1]]
y=[1,0,0,0,0,0,1,0,1,0]
clf=GaussianNB().fit(X,y)
p=[[1,0]]
print (clf.predict(p))
