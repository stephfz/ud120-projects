#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below

for point in data:
    salary = point[0]
    bonus = point[1]
    if salary != 26704229.0:
        matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
#matplotlib.pyplot.show()

#4 outliers
#salary > 1000000.0
salaries = []
for key in data_dict.keys():
    #print data_dict[key]['salary']

    #if data_dict[key]['salary']!= "NaN" and data_dict[key]['salary'] > 1000000:
        #print 'salary ', key, ' =', data_dict[key]['salary']
    if data_dict[key]['exercised_stock_options']!= "NaN":
        salaries.append(data_dict[key]['exercised_stock_options'])
salaries.sort()
print salaries
