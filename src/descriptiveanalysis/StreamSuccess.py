import pandas

import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns

sns.set(style="darkgrid")

#Plot Stream Vs Success
#Input : preprocessed_student_details.csv
#Output : results/descriptiveanalysis/StreamSuccess.PNG
#Columns Age,Course, Stream(A/L), Results Dimension Reduced,Gender,Success
names = ['Age','Course','Stream','Results', 'Gender','Success']

data = pandas.read_csv('preprocessed.csv')

cleanup_nums = {"Course":     {"Arts": 1, "Biological Science": 2 , "Commerce" : 3 , "Engineering Technology" : 4, 
                               "Physical Science" : 5 },

                "Success": {"yes": 1, "no": 0 }}

data.replace(cleanup_nums, inplace=True)

sns.catplot(x="Stream",hue='Success', kind="count" ,data=data ,aspect=2)