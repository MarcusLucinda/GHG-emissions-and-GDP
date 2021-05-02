# A comparison between developed countries and Latin America regarding GHG emissions and GDP predictions by 2100

## Please, click [here](https://htmlpreview.github.io/?https://raw.githubusercontent.com/marcusbonifacio/GHG-emissions-and-GDP/main/emissions_and_gdp.html?token=AMI4R7XVU4ZAOPWGPOIQZIS7S5NZU) to see the interactive maps, as it's not possible to display them here.


## Summary

- [Introduction](#introduction)
- [Sources](#sources)
- [Results](#results)
- [Conclusion](#conclusion)
- [References](#references)


## Introduction

Since the industrial revolution, humans have already thrown more than 1.5 tonnes of carbon dioxide on the atmosphere, with significant increase every year. Climate change consequences are perceptible and increasingly severe, with more common heat waves, desertification, floods and hurricanes.\
Although there is a consensus that the emissions should be reduced, even ratified through the Paris agreement, there's still a discussion of who's to blame. Developed countries state that they are creating and applying clean energy technologies, unlike developing countries, which state that they are industrializing and developed countries got rich in with high emissions in the past, and now it's their turn.\
Climate change also causes long term economic impacts, various predictions try to answer how the countries wealth will respond to the new reality. Several analyses point that developed countries will suffer softer impacts than underdeveloped ones.


## Sources

It was used consumption-based accounting for per capita CO2 emissions./
On behalf of GDP projections in was used Marshall Burke's and his collaborators paper./
All source where the data got scraped are listed at the end.


## Results

### Carbon dioxide emission

Countries that emitted most CO2 in 2016
```python
plt.figure(figsize=(10, 12))
plt.title("Países com maiores emissões de CO2")
plt.barh(countries, emissions)
plt.gca().invert_yaxis()
plt.xlabel("Emissões (ton per capita)")
```
![](/graphics/maiores_emissoes.png)



Emissions comparison between developed countries (blue) and Latin America (orange)
```python
plt.figure(figsize=(15, 100))
plt.barh(comp.index, comp.Emissions, align="center")
plt.gca().invert_yaxis()
plt.axvline(20)
plt.title('Developed and LatAm countries emissions (2016)')
plt.xlabel('Emissions (tonnes per capita)')
```
![](/graphics/comparacaoc.png)



Emissions map of 2016
```python
shapefile = './/ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp'
gdf = gpd.read_file(shapefile)[['ADMIN', 'ADM0_A3', 'geometry']]
gdf.columns = ['country', 'country_code', 'geometry']
gdf = gdf.drop(gdf.index[159])

df = pd.read_csv('to_map.csv')
merged = gdf.merge(df, left_on='country', right_on='Country')
merged_json = json.loads(merged.to_json())
json_data = json.dumps(merged_json)
geosource = GeoJSONDataSource(geojson = json_data)
palette = brewer['OrRd'][8]
palette = palette[::-1]
tick_labels = {'20': '>20'}
color_mapper = LinearColorMapper(palette = palette, low = 0, high = 20)
color_bar = ColorBar(color_mapper=color_mapper, label_standoff=8,width = 500, height = 20,
border_line_color=None,location = (0,0), orientation = 'horizontal', major_label_overrides = tick_labels)
hover = HoverTool(tooltips = [ ('Country/region','@country'),('Tons per capita', '@Emissions')])
p = figure(title = 'Emissões de CO2 baseadas em consumo em 2016 (toneladas per capita)', plot_height = 600 , plot_width = 950, toolbar_location = None, tools = [hover])
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None
p.axis.visible = False
p.patches('xs','ys', source = geosource,fill_color = {'field' :'Emissions', 'transform' : color_mapper},
          line_color = 'black', line_width = 0.25, fill_alpha = 1)
p.add_layout(color_bar, 'below')
```
![](/graphics/mapa2.png)



Box plot of 2016 world's emissions
```python
sns.set_theme(style="whitegrid")
plt.subplot()
ax = sns.boxplot(data=[south.Emissions, north.Emissions, asia.Emissions, middle.Emissions, africa.Emissions, oceania.Emissions, europe.Emissions], width=0.3)
plt.setp(ax.get_xticklabels(), rotation=45)
ax.set(ylabel='Emissões (tons per capita)',
xticklabels=['Am. do Sul', 'Am. do Norte', 'Ásia', 'Oriente Médio', 'África', 'Oceania', 'Europa'])
```
![](/graphics/continentes_emissoes.png)



### Economic Impacts

Most positive GDP variations to 2100
```python
plt.figure(figsize=(10, 12))
plt.title('Melhores variações de PIB para 2100')
plt.barh(countries_name, countries_gdp)
plt.gca().invert_yaxis()
```
![](/graphics/melhores_pib.png)



Most negative GDP variations to 2100
```python
plt.figure(figsize=(10, 12))
plt.subplot()
plt.title('Países com as piores variações de PIB para 2100')
plt.barh(countries_name_low, countries_gdp_low)
plt.gca().invert_xaxis()
```
![](/graphics/piores_pib.png)



GDP variation to 2100
```python
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
p = figure(title = 'Projeção de variação no PIB per capita para 2100', plot_height = 600 , plot_width = 950, toolbar_location = None, tools = [hover])
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None
p.axis.visible = False
p.patches('xs','ys', source = geosource,fill_color = {'field' :'GDP', 'transform' : color_mapper},
          line_color = 'black', line_width = 0.25, fill_alpha = 1)
p.add_layout(color_bar, 'below')
```
![](/graphics/mapa1.png)



Box plot of economic impacts to 2100
```python
sns.set_theme(style="whitegrid")
plt.subplot()
ax = sns.boxplot(data=[south.GDP, north_gdp.GDP, asia.GDP, middle.GDP, africa.GDP, oceania.GDP, europe.GDP], width=0.3)
plt.setp(ax.get_xticklabels(), rotation=45)
ax.set(ylabel='Variação no PIB per capita (%)',
xticklabels=['Am. do Sul', 'Am. do Norte', 'Ásia', 'Oriente Médio', 'África', 'Oceania', 'Europa'],
yticklabels=['-200', '-100', '0', '100', '200', '300', '400', '500'])
```
![](/graphics/continentes_gdp.png)



Relation between emissions and economic impact
```python
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
```
![](/graphics/comparacaoe.png)



## Conclusion

The countries geographic positions have large influence in this projection, northern hemisphere countries greatly contribute for climate change and will suffer less impacts. Tropical zone and southern hemisphere countries, especially Latin America and Africa, will be disproportionately harmed, since they have small contributions on emissions but will suffer the biggest economic impacts. The middle east has high emission rates and will suffer severe impacts.


## References

BURKE, M.; HSIANG, S.; MIGUEL, E. Global non-linear effect of temperature on economic production. Nature, v. 527. p. 235-239, 2015.
OUR WORLD IN DATA. Are consumption-based CO₂ per capita emissions above or below the global average?
