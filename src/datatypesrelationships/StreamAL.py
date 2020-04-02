import pandas as pd
import matplotlib.pyplot as plt


#Input preprocessed_student_details_f1.csv
#Results : results\datatypesrelationships\Stream.JPG

df = pd.read_csv("preprocessed_student_details_f1.csv")
gk = df.groupby('StreamAL')
print(gk.StreamAL.count())

# Data to plot
labels = 'Arts', 'Biological Science', 'Commerce', 'Engineering Technology', 'Physical Science'
sizes = gk.StreamAL.count()
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'green']

# Plot
plt.pie(sizes, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()