import osgeo.ogr

shapeFile = osgeo.ogr.Open("tl_2012_us_state.shp")
numLayers = shapeFile.GetLayerCount()

print ("Shapefile contains " + str(numLayers) + " layers.")

for layerNum in range (numLayers):
   layer = shapeFile.GetLayer(layerNum)
   spatialRef = layer.GetSpatialRef().ExportToProj4()
   numFeatures = layer.GetFeatureCount()
   print("Layer " + str(layerNum) + " has spatial reference " + spatialRef)
   print("Layer " + str(layerNum) + " has " + str(numFeatures) + " features:")
   print

   for featureNum in range (numFeatures):
      feature = layer.GetFeature (featureNum)
      featureName = feature.GetField("NAME")
      print("Feature " + str(featureNum) + " has name " + featureName) 
