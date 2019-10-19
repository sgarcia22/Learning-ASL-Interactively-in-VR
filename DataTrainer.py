#Python 3.7
import sys, os
import operator
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn import svm, preprocessing
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import average_precision_score, precision_recall_curve, accuracy_score

####################################################################
#Best Parameters: {'C': 100, 'gamma': 0.0001, 'kernel': 'rbf'}
#Best Estimators: SVC(C=100, cache_size=200, class_weight=None, coef0=0.0,
#    decision_function_shape='ovr', degree=3, gamma=0.0001, kernel='rbf',
#    max_iter=-1, probability=False, random_state=None, shrinking=True,
#    tol=0.001, verbose=False)
####################################################################
alphabet = list("abcdefghijklmnopqrstuvwxyz")

df = pd.read_csv("data.csv", index_col=0)
characters = df.index.values
columns = df.columns[1:]
x_train, x_test, y_train, y_test = train_test_split(df, characters, test_size = 0.25, train_size=0.75, random_state=0)
#Preprocess data
#scaler = preprocessing.StandardScaler().fit(x_train)
#x_train = scaler.transform(x_train)
#print(x_train)
#x_train = preprocessing.normalize(x_train)
#x_test = preprocessing.normalize(x_test)

####Used to get best parameters

#different_params = [{'kernel': ['rbf'], 'gamma': [1, 0.1, 0.01, 0.001, 0.00055, 0.0001, 0.00001, 10], 'C': [0.1, 1, 10, 50, 100]}]
#clf_grid = GridSearchCV(svm.SVC(), different_params, cv=5, verbose=1) #cv
#clf_grid.fit(x_train, y_train)
#print("Best Parameters:\n", clf_grid.best_params_)
#print("Best Estimators:\n", clf_grid.best_estimator_)

#### 

#Gamma is the amount of stretching in the z direction (dimensions)
#C parameter is the tradeoff, when C is large, it tries to classify many more examples correctly by having a smaller margin hyperplane 
clf = svm.SVC(kernel='rbf', C = 100.0, gamma=0.00055,probability=True) #Radial Basis Function Kernel with best results
clf.fit(x_train, y_train)
print(clf.score(x_train, y_train))
#x_test = scaler.transform(x_test)
print(clf.score(x_test, y_test))
#clf_predictions = clf.predict(x_test)

#Type I Error: False Positive, 
#Type II Error: False Negative,
#Precision: True Positive / (True Positive + False Postive)
#Recall: True Positive / (True Positive + False Negative)
#Accuracy: (True Positive + True Negative) / Total

#_score = clf.decision_function(x_test)
#average_precision = average_precision_score(y_test, y_score)
#print(average_precision)
#precision, recall, _ = precision_recall_curve(y_test, y_score)
#print (accuracy_score(y_test, y_score))
#clf.predict([[-0.8, -1]]))
df = pd.read_csv("testing_data.csv", index_col=0)
temp_index = 0
#Test Set
for index, row in df.iterrows():
    prediction = clf.predict_proba([row])
    prediction = prediction.flatten()
    max_value = max(prediction)
    max_index = np.argmax(prediction)
    print("Actual Letter: ", alphabet[temp_index], " | Predicted Letter: ", alphabet[max_index], " | ", alphabet[temp_index] == alphabet[max_index]," | Confidence: ", max_value * 100)
    temp_index += 1