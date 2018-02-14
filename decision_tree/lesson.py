from os import path
import sys
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )


from choose_your_own.class_vis import prettyPicture, output_image
from choose_your_own.prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl


features_train, labels_train, features_test, labels_test = makeTerrainData()



#################################################################################


########################## DECISION TREE #################################


# create/fit the classifier
from sklearn import tree

clf2 = tree.DecisionTreeClassifier(min_samples_split=2)
clf2.fit(features_train, labels_train)
clf50 = tree.DecisionTreeClassifier(min_samples_split=50)
clf50.fit(features_train, labels_train)

# preds
pred2 = clf2.predict(features_test)
pred50 = clf50.predict(features_test)

#prettyPicture(clf, features_test, labels_test)
#plt.show()

# accuracy
from sklearn.metrics import accuracy_score
acc_min_samples_split_2 = accuracy_score(pred2, labels_test)
acc_min_samples_split_50 = accuracy_score(pred50, labels_test)

print acc_min_samples_split_2
print acc_min_samples_split_50
