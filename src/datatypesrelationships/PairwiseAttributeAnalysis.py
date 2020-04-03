import pandas as pd
import matplotlib.pyplot as plt
import pandas
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")

#Input preprocessed_student_details_f1.csv
#Results : results\datatypesrelationships\pairwiserelationships.JPG

df = pd.read_csv("/content/preprocessed_student_details_f1.csv")

cleanup_nums = {"Course":  {"Software Engineering": 1, "Application Development": 2 , "Network Engineering" : 3 , "Accounting" : 4, 
                               "Business Management" : 5 }}

df.replace(cleanup_nums, inplace=True)

cleanup_nums1 = {"Gender":  {"Male": 1, "Female": 2 }}

df.replace(cleanup_nums1, inplace=True)

g = sns.pairplot(df, kind="reg")

g.savefig('save_as_a_png.png')