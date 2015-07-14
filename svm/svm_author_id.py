#!/usr/bin/python

""" 
    this is the code to accompany the Lesson 2 (SVM) mini-project

    use an SVM to identify emails from the Enron corpus by their authors
    
    Sara has label 0
    Chris has label 1

"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
clf = SVC(kernel = 'rbf', C = 10000)
t0 = time()
#Speeding up the algoorithm by training on a smaller dataset
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]
clf.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"
t0 = time()
pred = clf.predict(features_test)
print "predicting time:", round(time()-t0, 3), "s"
acc = accuracy_score(pred, labels_test)
print "Accurace of the SVM model = ", acc
answer10 = pred[10]
print "10th =",answer10
answer26 = pred[26]
print "26th =",answer26
answer50 = pred[50]
print "50th =",answer50
chris = 0
for i in pred:
	if i == 1:
		chris += 1
print "Number of emails predicted to be from Chris are : ",chris
#########################################################


