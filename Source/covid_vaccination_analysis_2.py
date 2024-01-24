#Create a daily vaccination report country wise


from datetime import datetime as dt
from bokeh.models.tickers import DaysTicker
import pandas as pd
from bokeh.io import output_file,show
from bokeh.plotting import figure
from bokeh.models import DatetimeTickFormatter, NumeralTickFormatter

#read CSV 

df = pd.read_csv("country_vaccinations.csv",parse_dates=['date'])

# selecting rows based on condition

country_x = df[df.iso_code.str.contains('ISR',case=False)]

x = country_x['date']

print(x)

y = country_x['daily_vaccinations_raw']/100000

output_file("daily country tracker.html")

f = figure(
            x_axis_type = 'datetime',
            sizing_mode='stretch_width'
     
        )
f.title.text = "Vaccination Tracker"
f.xaxis.axis_label="Date"
f.yaxis.axis_label="Doses in Million"

f.line(x,y,line_color="orange", line_width=2,legend_label="ISR")
f.circle(x,y,color='blue',legend_label="ISR")

f.legend.location = "bottom_left"
f.xaxis[0].formatter = DaysTicker()
show(f)





