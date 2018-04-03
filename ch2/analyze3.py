import osgeo.ogr

def analisaGeometria(geometria, indent=0):
   s = []
   s.append(" " * indent)
   s.append(geometria.GetGeometryName())
   if geometria.GetPointCount() > 0:
      s.append(" com " + str(geometria.GetPointCount()) + " pontos de dados")
   if geometria.GetGeometryCount() > 0:
      s.append(" contendo:")

   print ("".join(s))
   
   for i in range(geometria.GetGeometryCount()):
      analisaGeometria(geometria.GetGeometryRef(i), indent+1)

shapefile = osgeo.ogr.Open("tl_2012_us_state.shp")
camada = shapefile.GetLayer(0)
feicao = camada.GetFeature(2)
geometria = feicao.GetGeometryRef()
analisaGeometria (geometria)
