import pandas

import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

from plotly.offline import init_notebook_mode, iplot, plot
import plotly as py
init_notebook_mode(connected=True)
import plotly.graph_objs as go

import plotly.figure_factory as ff

#Input : preprocessed_student_details_f1.csv
$Output : results/descriptiveanalysis/CourseALPerfomance.PNG

df = pandas.read_csv('preprocessed_student_details_f1.csv')

import plotly.io as pio

Course = df.Course
perormance = df.ALPerformance

data = [dict(
  type = 'scatter',
  x = Course,
  y = perormance,
  mode = 'markers',
  transforms = [dict(
    type = 'groupby',
    groups = stream,
    styles = [
        dict(target = 'Software Engineering', value = dict(marker = dict(color = 'blue'))),
        dict(target = 'Application Development', value = dict(marker = dict(color = 'red'))),
        dict(target = 'Network Engineering', value = dict(marker = dict(color = 'black'))),
        dict(target = 'Business Management', value = dict(marker = dict(color = 'green'))),
        dict(target = 'Accounting', value = dict(marker = dict(color = 'yellow')))
    ]
  )]
)]

fig_dict = dict(data=data)
pio.show(fig_dict, validate=False)