import geopandas as gpd
import pandas as pd
import json
from bokeh.io import show
from bokeh.plotting import figure
from bokeh.models import GeoJSONDataSource, LinearColorMapper, ColorBar, HoverTool
from bokeh.palettes import brewer


shapefile = './/ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp'
gdf = gpd.read_file(shapefile)[['ADMIN', 'ADM0_A3', 'geometry']]
gdf.columns = ['country', 'country_code', 'geometry']
gdf = gdf.drop(gdf.index[159])

df = pd.read_csv('to_map.csv')
df["GDP"] = round(100 * df["GDP"], 0)
merged = gdf.merge(df, left_on='country', right_on='Country')
merged_json = json.loads(merged.to_json())
json_data = json.dumps(merged_json)
geosource = GeoJSONDataSource(geojson = json_data)
palette = brewer['RdBu'][9]
palette = palette[::-1]
tick_labels = {'100': '>100'}
color_mapper = LinearColorMapper(palette = palette, low = -100, high = 100)
color_bar = ColorBar(color_mapper=color_mapper, label_standoff=8,width = 500, height = 20,
border_line_color=None,location = (0,0), orientation = 'horizontal', major_label_overrides = tick_labels)
hover = HoverTool(tooltips = [ ('Country/region','@country'),('GDP variation', '@GDP %')])
p = figure(title = 'GDP variation to 2100', plot_height = 600 , plot_width = 950, toolbar_location = None, tools = [hover])
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None
p.patches('xs','ys', source = geosource,fill_color = {'field' :'GDP', 'transform' : color_mapper},
          line_color = 'black', line_width = 0.25, fill_alpha = 1)
p.add_layout(color_bar, 'below')

show(p)
