import pandas as pd
import matplotlib.pyplot as plt

#Input preprocessed_student_details_f1.csv
#Results : results\datatypesrelationships\Course.JPG

df = pd.read_csv("preprocessed_student_details_f1.csv")
gk = df.groupby('Course')
print(gk.Course.count())

# Data to plot
labels = 'Accounting', 'Application Development', 'Business Management', 'Network Engineering', 'Software Engineering'
sizes = gk.Course.count()
colors = ['gold', 'yellowgreen','red','blue',]

# Plot
plt.pie(sizes, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()
