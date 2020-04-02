import pandas

import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns

sns.set(style="darkgrid")

#Plot Course Vs Success
#Input : preprocessed_student_details.csv
#Output : results/descriptiveanalysis/CourseSuccess.PNG

#Columns Age,Course, Stream(A/L), Results Dimension Reduced,Gender,Success
names = ['Age','Course','Stream','Results', 'Gender','Success']

data = pandas.read_csv('preprocessed.csv')

cleanup_nums = {"Course":     {"AAT": 1, "Accounting": 2 , "Application Development" : 3 , "Automobile Eng" : 4, 
                               "Business Management" : 5, "Col Management" : 6, "Computer Instructor" : 7, "Computing" : 8, "Marine Eng" : 9 , "MSc in  App.Chemistry" : 10,
                              "Msc Reading -UoM" : 11, "Network Engineering" : 12, "Phd Reading" : 13 , "Shipping" : 14 ,  "Software Engineering" : 15 },

                "Success": {"yes": 1, "no": 0 }}

data.replace(cleanup_nums, inplace=True)

sns.catplot(x="Course",hue='Success', kind="count" ,data=data ,aspect=6)