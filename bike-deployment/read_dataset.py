
import pandas as pd

#Uncomment these three lines if you are not visualizing the data
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import shapefile

df = pd.read_csv("NYC-CitiBike-2016.csv")

df['starttime'] = pd.to_datetime(df['starttime'],infer_datetime_format=True)
df['stoptime'] = pd.to_datetime(df['stoptime'],infer_datetime_format=True)


#Visualization begins
#This code plots the latest location of the bikes on the map of New York
lons = [df[df['bikeid'] == i].sort_values('stoptime',ascending = False)['end station longitude'].iloc[0] for i in df['bikeid'].unique()]
lats = [df[df['bikeid'] == i].sort_values('stoptime',ascending = False)['end station latitude'].iloc[0] for i in df['bikeid'].unique()]

title = 'New York Bikeshare'
description = 'Bikes in a bikeshare scheme in New York'
shpfile = 'shp_folder/new_york'
fontcolor='#666666'

fig = plt.figure(figsize=(28, 20))
ax = fig.add_subplot(111, frame_on=False)
fig.suptitle(title, fontsize=50, y=.94, color=fontcolor)

sf = shapefile.Reader(shpfile)

x0, y0 ,x1, y1 = sf.bbox
cx, cy = (x0 + x1) / 2, (y0 + y1) / 2

m = Basemap(llcrnrlon=x0, llcrnrlat=y0, urcrnrlon=x1, urcrnrlat=y1, lat_0=cx, lon_0=cy, resolution='c', projection='mill')

m.readshapefile(shpfile, 'new_york', linewidth=.15)

x,y = m(lons,lats)
m.plot(x, y, 'bo', markersize=4)

plt.annotate(description, xy=(.58, 0.005), size=16, xycoords='axes fraction', color=fontcolor)
plt.show()
#End of visualization
