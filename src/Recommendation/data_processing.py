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
#stream = df.groupby('Stream(A//L,O/L)').sum()


# Feature extraction

#feature_cols = ['Age']

#conv_num = {"Gender" : {"Male":0 ,"Female":1},   }

# Feature Engineering - Unsupervised learning




# Supervised Machine learning

# Recommendation