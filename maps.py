import geopandas as gpd
import pandas as pd

shapefile = './/ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp'
gdf = gpd.read_file(shapefile)[['ADMIN', 'ADM0_A3', 'geometry',]]
gdf.columns = ['country', 'country_code', 'geometry']
gdf = gdf.drop(gdf.index[159])

df = pd.read_csv('to_map.csv')
merged = gdf.merge(df, left_on='country', right_on='Country')
print(merged)