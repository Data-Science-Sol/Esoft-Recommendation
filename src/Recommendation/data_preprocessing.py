# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 07:46:43 2020

@author: achin
"""
"""
Data Science Project 
"""

import pandas as pd

# Data Preprocessing
#%%
df = pd.read_csv('Student Details - Sheet1.csv')


is_SE = df['Course']=='Software Engineering'

df_SE = df[is_SE]

# Correcting user input for A/L Stream

con_stream = {"Stream(A//L,O/L)":{"A/L - Bio":"Biological Science","A/L Bio":"Biological Science"
              ,"A/L-Bio":"Biological Science","A/L - Maths":"Physical Science",
              "A/L Maths":"Physical Science","A/L- Maths":"Physical Science",
              "A/L-Maths":"Physical Science","A/L Arts":"Arts","A/L Commerce":"Commerce",
              "A/L commerce":"Commerce","A/L-Commerce":"Commerce",
              "A/L-Commerce Stream":"Commerce","A/L- Engineering Technology ":"Engineering Technology",
              "A/L-E.tech":"Engineering Technology"}}

df.replace(con_stream, inplace=True)
df.to_csv('preprocessed_student_details.csv')

#%%

# Filtering Courses

df1 = pd.read_csv('C:/Users/achin/OneDrive - Imperial College London/Achintha/PhD/Data Science/Group project/Esoft-Recommendation/data/preprocessed_student_details_ach.csv')

con_course = {"Course":{"AAT":"Accounting","Computing":"Software Engineering","Software Enginnering":"Software Engineering"}}
df1.replace(con_course, inplace=True)


df2 = df1.loc[df1['Course'].isin(['Accounting','Application Development','Business Management','Network Engineering','Software Engineering'])]

df2.to_csv('C:/Users/achin/OneDrive - Imperial College London/Achintha/PhD/Data Science/Group project/Esoft-Recommendation/data/preprocessed_student_details_f1.csv',index = False)

#%%
# Encode categorical data in numerical values

df1 = pd.read_csv('C:/Users/achin/OneDrive - Imperial College London/Achintha/PhD/Data Science/Group project/Esoft-Recommendation/data/preprocessed_student_details_f1.csv')


#stream = df.groupby('Stream(A//L,O/L)').sum()


# Feature extraction

#feature_cols = ['Age']

#conv_num = {"Gender" : {"Male":0 ,"Female":1},   }

# Feature Engineering - Unsupervised learning




# Supervised Machine learning

# Recommendation