#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import pprint

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

'''
key in the dictionary is a person’s name and the 
value is a dictionary containing all the features of that person.
'''
count = 0
for key,value in enron_data.iteritems():
	if value['poi'] == True:
		count += 1
print "Total POI in the list are : ",count

pprint.pprint(enron_data.keys())

#Total stock value of James Prentice
print enron_data['PRENTICE JAMES']['total_stock_value']

#How many email messages do we have from Wesley Colwell to persons of interest?
print enron_data['COLWELL WESLEY']['from_this_person_to_poi']

#What’s the value of stock options exercised by Jeffrey Skilling?
print enron_data['SKILLING JEFFREY K']['exercised_stock_options']