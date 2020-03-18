import pandas

import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns

sns.set(style="darkgrid")

#Plot Results Vs Success
#Input : preprocessed_student_details.csv
#Output : results/ResultsSuccess.PNG
#Columns Age,Course, Stream(A/L), Results Dimension Reduced,Gender,Success
names = ['Age','Course','Stream','Results', 'Gender','Success']

data = pandas.read_csv('preprocessed.csv')

cleanup_nums = {"Success": {"yes": 1, "no": 0 }}

data.replace(cleanup_nums, inplace=True)

sns.catplot(x="ResultsDR",hue='Success', kind="count" ,data=data ,aspect=6)