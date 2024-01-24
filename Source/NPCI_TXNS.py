#This is a BOKEH Piechart example from real world data of NPCI ATM transactions

from bokeh.palettes import Category20c
from bokeh.plotting import figure, show
from bokeh.transform import cumsum
import pandas as pd
from math import pi

#Get the CSV into a DataFrame

df = pd.read_csv("txns.csv")

#Pie chart, where the slices will be ordered and plotted counter-clockwise:

#GET the CSV data into a DICT variable.

x = dict(df.values)

#print(type(x)) #to be used to check if X is indeed DICT variable.


data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'name'})

data['angle'] = data['value']/data['value'].sum() * 2*pi
data['color'] = Category20c[len(x)]


p = figure(height=500, title="Pie Chart", toolbar_location=None,
           tools="hover", tooltips="@name: @value", x_range=(-0.5, 1.0))


p.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend_field='name', source=data)

p.axis.axis_label = None
p.axis.visible = False
p.grid.grid_line_color = None

show(p)


