import pandas as pd
import matplotlib.pyplot as plt

#Input preprocessed_student_details_f1.csv
#Results : results\datatypesrelationships\Gender.JPG

df = pd.read_csv("preprocessed_student_details_f1.csv")
gk = df.groupby('Gender')
print(gk.Gender.count())

# Data to plot
labels = 'Male', 'Female'
sizes = gk.Gender.count()
colors = ['gold', 'yellowgreen']

# Plot
plt.pie(sizes, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()