
import matplotlib.pyplot as pl

import pandas

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Describe Data
#Input : StudentDetails.csv in data folder
#Results : DataDescribe.png

sns.set(style="darkgrid")

names = ['Course-Catagory','stream-catagory','result-scale','future-succes']

data = pandas.read_csv('StudentDetails.csv')

data.info()

data.shape