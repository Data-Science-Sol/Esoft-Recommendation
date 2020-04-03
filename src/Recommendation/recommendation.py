# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 10:17:41 2020

@author: achin
"""

import matplotlib.pyplot as plt


import pandas as pd

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from joblib import dump
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier

#%%

data = pd.read_csv('C:/Imperial Drive/Achintha/PhD/Data Science/Group project/Esoft-Recommendation/data/preprocessed_student_details_numeric_normalized.csv')


con_course = {"Course":{"Accounting":1,"Software Engineering":2,"Application Development":3,"Network Engineering":4,"Business Management":5}}
data.replace(con_course, inplace=True)




#%%

X = data.drop(columns=['Student', 'Course']) 
X_withID = data.drop(columns=[ 'Course']) 
y = data.Course

clf = MultinomialNB()
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)


model = clf.fit(X_train, y_train)

print(model.predict_proba(X_test))


#%%


X_withID = data.drop(columns=[ 'Course']) 
y_withID = data.loc[:,['Student','Course']]

#clf = MultinomialNB()
X_train, X_test, y_train, y_test = train_test_split(X_withID,y_withID, test_size=0.2)

train = X_train
train['Course']= y_train ['Course']
train.to_csv('C:/Imperial Drive/Achintha/PhD/Data Science/Group project/Esoft-Recommendation/data/train.csv',index = False)


test = X_test
test['Course']= y_test ['Course']
test.to_csv('C:/Imperial Drive/Achintha/PhD/Data Science/Group project/Esoft-Recommendation/data/test.csv',index = False)
#model = clf.fit(X_train, y_train)

#print(model.predict_proba(X_test))

#%%

#model training

train = pd.read_csv('C:/Imperial Drive/Achintha/PhD/Data Science/Group project/Esoft-Recommendation/data/train.csv')

X_train = train.drop(columns=['Student', 'Course']) 
y_train = train.Course
clf1 = MultinomialNB()
clf2 = KNeighborsClassifier(5)


model1 = clf1.fit(X_train,y_train)
model2 = clf2.fit(X_train,y_train)

#%%


test = pd.read_csv('C:/Imperial Drive/Achintha/PhD/Data Science/Group project/Esoft-Recommendation/data/test.csv')

X_test = test.drop(columns = ['Student', 'Course'])
y_test = test.Course


pred_probs1 = model1.predict_proba(X_test)
pred_probs2 = model2.predict_proba(X_test)

predictions =[]

for i in range(len(test)):
    recommentations = []
    for j in range(5):
        if pred_probs2[i][j]>0:
            recommentations.append(j+1)
    
    predictions.append(recommentations)

correct_predictions = 0

for i in range(len(test)):
    if y_test[i] in predictions[i]:
        correct_predictions = correct_predictions + 1

Accuracy = correct_predictions/len(test)
print(Accuracy)
#%%


dump(model, 'C:/Imperial Drive/Achintha/PhD/Data Science/Group project/Esoft-Recommendation/multinomialNB.joblib')
dump(model2, 'C:/Imperial Drive/Achintha/PhD/Data Science/Group project/Esoft-Recommendation/KnearestNeighbour.joblib')








