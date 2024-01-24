#Analyse the weather data

import pandas as pd
from bokeh.plotting import figure
from bokeh.io import show,output_file

#read the excel 

df = pd.read_excel("Weather_data.xlsx")

t_list = df["Temperature"]
p_list = df["Pressure"]

#lambda function to divide all List elements by 10

t = [i/10 for i in t_list] 
p = [i/10 for i in p_list]   

#Open output file

output_file("Temp_vs_Pressure.html")

#create the figure

f = figure(plot_width = 600,plot_height = 500)

f.title.text="Temperature and Air Pressure"
f.title.text_color="Gray"
f.title.text_font="Arial"
f.title.text_font_style="italic"
f.xaxis.minor_tick_line_color=None
f.yaxis.minor_tick_line_color=None
f.xaxis.axis_label="Temperature"
f.yaxis.axis_label="Pressue(hPa)"    

 

#plot the graph

#f.circle(t,p)

f.dot(t,p)

show(f)

