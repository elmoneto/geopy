import osgeo.ogr

shapeFile = osgeo.ogr.Open("tl_2012_us_state.shp")
qtdeCamadas = shapeFile.GetLayerCount()

print ("Shapefile contém " + str(qtdeCamadas) + " camadas.")

for numeroCamada in range (qtdeCamadas):
   camada = shapeFile.GetLayer(numeroCamada)
   refEspacial = camada.GetSpatialRef().ExportToProj4()
   qtdeFeicoes = camada.GetFeatureCount()
   print("Camada " + str(numeroCamada) + " tem referência espacial " + refEspacial)
   print("Camada " + str(numeroCamada) + " tem " + str(qtdeFeicoes) + " feições:")
   print

   for numeroFeicao in range (qtdeFeicoes):
      feicao = camada.GetFeature(numeroFeicao)
      nomeFeicao = feicao.GetField("NAME")
      print("Feição " + str(numeroFeicao) + " tem nome " + nomeFeicao) 
