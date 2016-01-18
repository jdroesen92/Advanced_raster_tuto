import os
import mapnik
os.chdir('/home/user/git/geoScripting/Python_intro')

## Loading osgeo
from osgeo import ogr, osr

## Is the ESRI Shapefile driver available?
driverName = "ESRI Shapefile"
drv = ogr.GetDriverByName( driverName )

## choose your own name
## make sure this layer does not exist in your 'data' folder
fn = "location.shp"
layername = "locations1"

## Create shape file
ds = drv.CreateDataSource(fn)
print ds.GetRefCount()

# Set spatial reference
spatialReference = osr.SpatialReference()
spatialReference.ImportFromProj4('+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs')

## Create Layer
layer=ds.CreateLayer(layername, spatialReference, ogr.wkbPoint)
print(layer.GetExtent())

## Create a point
Mex = ogr.Geometry(ogr.wkbPoint)
Wag = ogr.Geometry(ogr.wkbPoint)

## SetPoint(self, int point, double x, double y, double z = 0)
Mex.SetPoint(0, -99.123008, 19.388826) 
Wag.SetPoint(0, 5.655079,51.963486)

## Feature is defined from properties of the layer:e.g:

layerDefinition = layer.GetLayerDefn()
feature1 = ogr.Feature(layerDefinition)
feature2 = ogr.Feature(layerDefinition)

## Lets add the points to the feature
feature1.SetGeometry(Mex)
feature2.SetGeometry(Wag)

## Lets store the feature in a layer
layer.CreateFeature(feature1)
layer.CreateFeature(feature2)
print "The new extent"
print layer.GetExtent()

ds.Destroy()

## instruction for opening shapefile in QGIS
qgis.utils.iface.addVectorLayer(fn, layername, "ogr") 
aLayer = qgis.utils.iface.activeLayer()
print aLayer.name()

#put shapefile in KML
pointslayer =  QgsVectorLayer('/home/user/git/geoScripting/Python_intro/location.shp', 'locations1' , "ogr")
pointslayer.isValid()
dest_projection = QgsCoordinateReferenceSystem(4326)
QgsVectorFileWriter.writeAsVectorFormat(pointslayer, '/home/user/git/geoScripting/Python_intro/Locations.kml', 'utf-8', dest_projection, 'KML' )