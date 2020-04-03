import pandas

import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns

#Input : CourseGenderTotalPreprocessed.csv
#Output : GenderCourseRelationShip.png

data = pandas.read_csv('/content/CourseGenderTotalPreprocessed.csv')

fig_dims = (20, 5)
fig, ax = plt.subplots(figsize=fig_dims)

sns.barplot(x="Course", y="Total", hue="Gender",ax=ax, data=data)