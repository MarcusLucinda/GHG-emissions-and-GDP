import pandas as pd
import matplotlib.pyplot as plt
'''
ghg = pd.read_csv('ghg_emissions.csv')
countries = ghg.Country.to_list()
countries = countries[:30]
emissions = ghg.Emissions.to_list()
emissions = emissions[:30]

plt.figure(figsize=(10, 12))
plt.subplot()
plt.barh(countries, emissions)
plt.gca().invert_yaxis()
plt.show()
'''
'''
gdp = pd.read_csv('gdp.csv')
countries_name = gdp.Country.to_list()
countries_name = countries_name[:20]
countries_gdp = gdp.GDP.to_list()
countries_gdp = countries_gdp[:20]

plt.figure(figsize=(10, 12))
plt.subplot()
plt.barh(countries_name, countries_gdp)
plt.gca().invert_yaxis()
plt.show()
'''
'''
gdp = pd.read_csv('gdp.csv')
countries_name_low = gdp.Country.to_list()
countries_name_low = countries_name_low[-20:]
countries_gdp_low = gdp.GDP.to_list()
countries_gdp_low = countries_gdp_low[-20:]

plt.figure(figsize=(10, 12))
plt.subplot()
plt.barh(countries_name_low, countries_gdp_low)
plt.gca().invert_xaxis()
plt.show()
'''

north = pd.read_csv('developed.csv')
latin = pd.read_csv('latin.csv')
north = north.drop('index', 1)
north = north.set_index('Country')
latin = latin.drop('index', 1)
latin = latin.set_index('Country')
#countries_north = north.Country.to_list()
#countries_latin = latin.Country.to_list()
emissions_latin = latin.Emissions.to_list()
emissions_north = north.Emissions.to_list()
print (north)


plt.figure(figsize=(10, 12))
#plt.subplot()
plt.bar(emissions_north, north.index.values, color='r')
plt.bar(emissions_latin, latin.index.values, color='g')
plt.show()

'''
df = pd.DataFrame({'a' : [2,6,2,4,5,3,7]})
t1 = df[df['a']<5]
t2 = df[df['a']>=5]
'''