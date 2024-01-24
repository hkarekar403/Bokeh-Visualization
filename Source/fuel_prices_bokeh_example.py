#This is the basic code for a line graph

import bokeh
from bokeh.plotting import figure
from bokeh.io import output_file,show

import pandas

df = pandas.read_csv("RS_Session_252_AU_447.B.csv")

print(df)

mm_yr = []
fuel_price = []

mm_yr = df["Month-wise"]
print(mm_yr)

fuel_price = df["Petrol (Rs./litre)"]

print(fuel_price)

#prepare the output file

output_file("Fuel_price.html")

#create the figure object

mm_yr_range = mm_yr

f=figure(x_range=mm_yr)

#create the line plot

f.line(mm_yr,fuel_price)
show(f)
