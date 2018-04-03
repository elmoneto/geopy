import osgeo.ogr

shapefile = osgeo.ogr.Open("tl_2012_us_state.shp")
camada = shapefile.GetLayer(0)
feicao = camada.GetFeature(2)

print ("A feição 2 tem os seguintess atributos: ")
print

atributos = feicao.items()
print(atributos)

for chave,valor in atributos.items():
    print (str(chave) + " = " + str(valor))

geometria = feicao.GetGeometryRef()
geometriaNome = geometria.GetGeometryName()

print
print("Os dados de geometria da feição consistem em uma" + geometriaNome)
