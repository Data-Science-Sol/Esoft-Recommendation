import pandas as pd
import matplotlib.pyplot as plt

#Input preprocessed_student_details_f1.csv
#Results : results\datatypesrelationships\Subject2.JPG

df = pd.read_csv("preprocessed_student_details_f1.csv")
gk = df.groupby('ALSubject2')
print(gk.ALSubject2.count())

# Data to plot
labels = 'A', 'B', 'C', 'S' , 'W'
sizes = gk.ALSubject2.count()
colors = ['gold', 'yellowgreen', 'lightcoral', 'green', 'black']

# Plot
plt.pie(sizes, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()