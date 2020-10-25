import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
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

'''
comp = pd.read_csv('dev_and_latin.csv')
del comp['index']
comp.set_index('Country', inplace=True)

plt.figure(figsize=(15, 25))
plt.subplot()
plt.barh(comp.index, comp.Emissions, align="center")
plt.gca().invert_yaxis()
plt.tick_params(axis='y', labelsize=6)
plt.show()
'''
'''
dev = pd.read_csv('gdp_comp_dev.csv', index_col='Country')
latin = pd.read_csv('gdp_comp_latin.csv', index_col='Country')
df1 = pd.read_csv('gdp_comp.csv')
plt.figure(figsize=(15, 25))
plt.subplot()
plt.scatter(dev.Emissions, dev.GDP)
plt.scatter(latin.Emissions, latin.GDP)
z = np.polyfit(df1.Emissions, df1.GDP, 1)
p = np.poly1d(z)
plt.plot(df1.Emissions, p(df1.Emissions), "r")
plt.show()
'''
