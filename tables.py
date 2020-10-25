
import pandas as pd
import numpy as np
'''

file_name = './/ghg_emissions.csv'
table = pd.read_csv('ghg_emissions.csv', sep=',')
table['Emissions'] = table.Emissions.replace('-', np.nan).astype(float)
table["Emissions"].astype(float).fillna(0.0)
newtable = table.sort_values('Emissions', ascending=False)
newtable = newtable.reset_index(drop=True)
newtable.to_csv(file_name, sep=',')
'''
'''
file_name = './/gdp.csv'
gdp = pd.read_csv('gdp.csv', sep=',', index_col='index')
gdp = gdp.sort_values('GDP', ascending=False)
gdp = gdp.reset_index(drop=True)
print(gdp)
gdp.to_csv(file_name, sep=',')
'''
'''
file_name = './/gdp_comp.csv'
df1 = pd.read_csv('dev_and_latin.csv', sep=',', index_col='Country')
del df1['index']
df2 = pd.read_csv('gdp_del.csv', sep=',', index_col='Country')
del df2['index']
df3 = (df1.join(df2, how='outer'))
df3.to_csv(file_name, sep=',')
'''

file_name = './/to_map.csv'
df1 = pd.read_csv('gdp.csv', sep=',', index_col='Country')
del df1['index']
df2 = pd.read_csv('ghg_emissions.csv', sep=',', index_col='Country')
del df2['index']
df3 = (df1.join(df2, how='outer'))
df3.to_csv(file_name, sep=',')

print(df3)