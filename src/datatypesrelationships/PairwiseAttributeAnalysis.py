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

g = sns.pairplot(df, kind="reg",vars=["A/L Performance","Age"])