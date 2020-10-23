
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