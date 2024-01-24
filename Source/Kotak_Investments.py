from bokeh.palettes import Category20c
from bokeh.plotting import figure, show
from bokeh.transform import cumsum
import pandas as pd
from math import pi

df = pd.read_csv("equity-holding-data-2022-03-31.csv")

#the zip & dict gets 2 columns from the CSV and puts them into the Series to be used for PIE chart
x = dict(zip(df['Industry'],df['Qty']))

print(x)

data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'Qty'})

data['angle'] = data['value']/data['value'].sum() * 2*pi
data['color'] = Category20c[len(x)]



p = figure(width = 800,height=700, title="Pie Chart of all my investments", toolbar_location=None,
           tools="hover", tooltips="@Qty: @value", x_range=(-0.5, 1.5))


p.wedge(x=0.3, y=1, radius=0.5,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend_field='Qty', source=data)

p.axis.axis_label = None
p.axis.visible = False
p.grid.grid_line_color = None

show(p)
