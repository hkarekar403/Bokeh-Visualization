#Education data from csv

import pandas as pd

from bokeh.plotting import figure
from bokeh.io import output_file,show


#read the csv file using Pandas library

df = pd.read_csv("bachelors.csv")

#we have to select 2 columns from this csv
# 1 ) Year
# 2 ) Engineering

x = df["Year"]
y = df["Engineering"]



s = df["Year"]
t = df["Architecture"]

#create the output file

output_file("Edu_Data.html")

#create the figure

p = figure(plot_width = 600,plot_height = 500)
h = figure(plot_width = 600,plot_height = 500)

p.title.text="Cool Data"
p.title.text_color="Blue"
p.title.text_font="times"
p.title.text_font_style="bold"
p.xaxis.minor_tick_line_color=None
p.yaxis.minor_tick_line_color=None
p.xaxis.axis_label="Year"
p.yaxis.axis_label="Engineering"    
 

h.title.text="Architecture"
h.title.text_color="Orange"
h.title.text_font="times"
h.title.text_font_style="bold"
h.xaxis.minor_tick_line_color=None
h.yaxis.minor_tick_line_color=None
h.xaxis.axis_label="Year"
h.yaxis.axis_label="Architecture"    


p.line(x,y)
p.line(s,t)

show(h)

show(p)
