import pandas

import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns

sns.set(style="darkgrid")

#Plot Age Vs Success
#Input : preprocessed_student_details.csv
#Output : results/AgeSuccess.PNG
#Columns Age,Course, Stream(A/L), Results Dimension Reduced,Gender,Success

#Columns Age,Course, Stream(A/L), Results Dimension Reduced,Gender,Success
names = ['Age','Course','Stream','Results', 'Gender','Success']

data = pandas.read_csv('preprocessed.csv')

cleanup_nums = {"Success": {"yes": 1, "no": 0 }}

data.replace(cleanup_nums, inplace=True)

sns.catplot(x="Age",hue='Success', kind="count" ,data=data ,aspect=2)