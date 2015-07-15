#!/usr/bin/python

""" 
    this is the code to accompany the Lesson 3 (decision tree) mini-project

    use an DT to identify emails from the Enron corpus by their authors
    
    Sara has label 0
    Chris has label 1

"""
'''
Notes:
There is a trick to make non linear decision making using linear decision surface
DT - You can multiple questions one after the other.
Entropy - controls how a DT decides where to split the data



'''
'''
import sys
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl

features_train, labels_train, features_test, labels_test = makeTerrainData()



########################## DECISION TREE #################################


### your code goes here--now create 2 decision tree classifiers,
### one with min_samples_split=2 and one with min_samples_split=50
### compute the accuracies on the testing data and store
### the accuracy numbers to acc_min_samples_split_2 and
### acc_min_samples_split_50, respectively
from sklearn import tree
from sklearn.metrics import accuracy_score
clf = tree.DecisionTreeClassifier(min_samples_split = 2)
clf.fit(features_train,labels_train)
pred2 = clf.predict(features_test)
acc_min_samples_split_2 = accuracy_score(pred2, labels_test)

clf = tree.DecisionTreeClassifier(min_samples_split = 50)
clf.fit(features_train,labels_train)
pred50 = clf.predict(features_test)
acc_min_samples_split_50 = accuracy_score(pred50, labels_test)


def submitAccuracies():
  return {"acc_min_samples_split_2":round(acc_min_samples_split_2,3),
          "acc_min_samples_split_50":round(acc_min_samples_split_50,3)}
'''
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn import tree
from sklearn.metrics import accuracy_score

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
### your code goes here ###
clf = tree.DecisionTreeClassifier(min_samples_split = 40)
clf.fit(features_train,labels_train)
pred = clf.predict(features_test)
acc = accuracy_score(pred, labels_test)
print acc
print len(features_train[0])
#########################################################


