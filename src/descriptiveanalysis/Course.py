import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
%matplotlib inline

df = pandas.read_csv('preprocessed_student_details_f1.csv')

sns.pairplot(df, hue='Course');