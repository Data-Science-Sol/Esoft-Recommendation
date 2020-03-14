
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Analyze student future success and A/L results

#Input : student-analyase-succes-stream-course-results.csv in data folder

#Results : 

#result-success-box.png
#result-sucess-scatter-plot.png
#success-result-pipoint.png

sns.set(style="darkgrid")

names = ['Course-Catagory','stream-catagory','result-scale','future-succes']

data = pandas.read_csv('student-analyase-succes-stream-course-results.csv')

cleanup_nums = {"result-scale":     {"Good": 1, "": 2 , "Intermediate" : 2 , "Worse" : 3  },
                "future-succes": {"yes": 1, "no": 0 }}

data.replace(cleanup_nums, inplace=True)
sns.catplot(x="result-scale", y="future-succes", data=data);

sns.catplot(x="result-scale", y="future-succes", data=data, kind="box");

sns.catplot(x="result-scale", y="future-succes", data=data, kind="point");