import pandas as pd
import matplotlib.pyplot as plt
import pandas
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")

input : preprocessed_student_details_f1.csv
output : results\datatypesrelationships\pairwiserelationships.jpg

df = pd.read_csv("preprocessed_student_details_f1.csv")

cleanup_nums = {"Course":     {"Software Engineering": 1, "Application Development": 2 , "Network Engineering" : 3 , "Accounting" : 4, 
                               "Business Management" : 5 }}

df.replace(cleanup_nums, inplace=True)

g = sns.pairplot(df, kind="reg")

g.savefig('save_as_a_png.png')