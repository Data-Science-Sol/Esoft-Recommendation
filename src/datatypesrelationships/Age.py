import pandas as pd
import matplotlib.pyplot as plt
import pandas
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")

#Input preprocessed_student_details_f1.csv
#Results : results\datatypesrelationships\Age.JPG

df = pd.read_csv("preprocessed_student_details_f1.csv")
gk = df[['Age']]

sns.catplot(x="Age", kind="count" ,data=gk ,aspect=6)