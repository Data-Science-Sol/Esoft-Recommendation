import pandas

import matplotlib.pyplot as pl

import pandas

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#This uses csv file in data folder called student-analyase-succes-stream-course-results.csv
#Used this code to identify best variable that can help explain student future success
#Here students A/L result was identified as a ordinal variable and course-catagory and and stream as nominal data.
#Hence I have observed that, the student that score well in their A/L have a good chance in becoming successful in the future. 
# I have ignored gender and age because they are demographic data.

# Input : student-analyase-succes-stream-course-results.csv in data folder 

# Results

#Results-Success.png
#Course-Catagory-Success.png
#Stream-future-Success.png

sns.set(style="darkgrid")

names = ['Course-Catagory','stream-catagory','result-scale','future-succes']

data = pandas.read_csv('student-analyase-succes-stream-course-results.csv')

sns.catplot(x="Course-Catagory",hue='future-succes', kind="count" ,data=data ,aspect=2)

sns.catplot(x="stream-catagory",hue='future-succes', kind="count" ,data=data ,aspect=2)

sns.catplot(x="result-scale",hue='future-succes', kind="count" ,data=data ,aspect=2)