import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
%matplotlib inline

#Input : preprocessed_student_details_f1.csv
Output : StreamAL.png

df = pandas.read_csv('preprocessed_student_details_f1.csv')

sns.pairplot(df, hue='StreamAL');