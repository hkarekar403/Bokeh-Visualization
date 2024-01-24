#This is the basic code for a line graph

import bokeh
from bokeh.plotting import figure
from bokeh.io import output_file,show


day_of_the_week = [1,2,3,4,5,6,7]
doses_for_the_day = [3,5,10,13,6,9,7]

#prepare the output file

output_file("Graph.html")

#create the figure object

f=figure()

#create the line plot

f.triangle_pin(day_of_the_week,doses_for_the_day)
show(f)
