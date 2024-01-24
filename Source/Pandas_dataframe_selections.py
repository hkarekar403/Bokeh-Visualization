import pandas
import matplotlib.pyplot as plt
import matplotlib as mpl
from datetime import datetime

from datetime import datetime # required for getting data based on DATE & TIME

data = pandas.read_csv("equity-holding-data-2022-03-31.csv",parse_dates=['Date Invested'])


#create new dataframe QT where we take only those equity which has QTY less than 10
qt = data[data['Qty'] < 10]

#print(qt)

#create new dataframe SN where we only take conditional data from main dataframe DATA
sn = data[data['Security Name'].str.contains('BANK',na=False,case = False)]

##print(data.head())
#print(sn)

#create a dataframe DTD where we only take conditional data based on timestamp column of the dataframe
dtd = data[data['Date Invested'] > datetime(2016,7,1)]

#print(dtd['Date Invested'])

#create a dataframe using multiple conditions
#Date invested > (2016,7,1 ) and Qty > 10

multdf = data[(data['Qty'] > 10) &
     (data['Date Invested'] > datetime(2016,7,1))]
    
#print(multdf)


#Get the day from the date field and add a new column based on it

data2 = pandas.read_csv("country_vaccinations.csv",parse_dates=['date'])


# selecting rows based on condition

#country_x = data2[data2.iso_code.str.contains('IND',case=False)]
#country_y = data2[data2.iso_code.str.contains('BRA',case=False)]


#print(data2.head())

#country_x['day'] = country_x['date'].dt.dayofyear

#country_y['day'] = country_y['date'].dt.dayofyear


##print(country_x['week'])

#plt.plot(country_x.month,country_x['total_vaccinations'])


#plt.figure(figsize=(15,4))
#plt.xticks(country_x.day)
#plt.figlegend(country_x.day,"Day")

#plt.plot(country_x.day, country_x['total_vaccinations'])
#plt.plot(country_y.day, country_y['total_vaccinations'])

#plt.show()

#instead of writing the code twice we can use loop

#iso_code_x = ["IND", "CHN", "BRA","HKG","USA","ZWE"]

# 1  Get all the rows for iso_code into 1 new dataframe
# 2 Remove duplicates 
# 3 Move those into a Tuple

iso_code_x_df = data2['iso_code']

iso_codes_wo_dupl = iso_code_x_df.drop_duplicates()

#print(type(iso_codes_wo_dupl))
iso_code_x = list(iso_codes_wo_dupl)

iso_code_x = ["AUS","IND", "CHN", "BRA","HKG","USA","ZWE"]
#print(iso_code_x)

plt.figure(figsize=(30,5), dpi=120)
plt.xlabel('Day of Year--->')
plt.ylabel('Doses in Millions --->')
plt.title('Vaccines per country')


for isocode in iso_code_x:
     data2['day'] = data2['date'].dt.dayofyear
     country_x = data2.loc[data2.iso_code.str.contains(isocode,case=False)]
     plt.plot(country_x['day'], country_x['total_vaccinations'],label=isocode)

plt.legend(loc='lower right')
plt.show()


#Create a Pie chart using matplot lib(basic option)
#We will get a vaccination data for one country and then 
#try to plot a pie chart for various vaccines given in that country
