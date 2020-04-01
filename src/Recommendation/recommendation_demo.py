# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 12:50:35 2020

@author: achin
"""
from joblib import load
import numpy as np
#inputs 
stream = "Biological Science"
alresults1 = "B"
alresults2 = "C"
alresults3 = "S"
Gender = "Male"
Age = 24

# feature encoding

streamdic = {"Arts":0,"Commerce":1,"Biological Science":2,"Engineering Technology":3,"Physical Science":4}
resultdic = {"A":4,"B":3,"C":2,"S":1.5,"W":0}   
genderdic = {"Male":0,"Female":1} 

stream_en_norm = streamdic[stream]/4
alresults1_en = resultdic[alresults1]
alresults2_en = resultdic[alresults2]
alresults3_en = resultdic[alresults3]

alresults_en_norm = (alresults1_en+alresults2_en+alresults3_en)/12
genderen = genderdic[Gender]
age_norm = (Age-16)/14


#model predictions


model = load('C:/Imperial Drive/Achintha/PhD/Data Science/Group project/Esoft-Recommendation/multinomialNB.joblib') 
predictions = model.predict_proba(np.array([[stream_en_norm,alresults_en_norm,genderen,age_norm]]))

recommendations_list = ["Accounting","Software Engineering","Application Development","Network Engineering","Business Management"]
recommentation = []

for i in range(5):
    if predictions[0][i]>0.2:
        recommentation.append(recommendations_list[i])
print(predictions)
print(recommentation)
