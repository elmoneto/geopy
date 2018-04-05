import osgeo.ogr

def findPoints(geometria, resultados):
    for i in range(geometria.GetPointCount()):
        x,y,z = geometria.GetPoint(i)
        if (resultados['north'] == None) or (resultados['north'][1] < y):
            resultados['north'] = (x,y)
        if resultados['south'] == None or resultados['south'][1] > y:
            resultados['south'] = (x,y)
    for i in range(geometria.GetGeometryCount()):
        findPoints(geometria.GetGeometryRef(i), resultados)

shapefile = osgeo.ogr.Open("tl_2012_us_state.shp")
camada = shapefile.GetLayer(0)
feicao = camada.GetFeature(55)
geometria = feicao.GetGeometryRef()

resultados = {'north' : None,
            'south' : None}
findPoints(geometria,resultados)

print("Pontos mais ao norte é " + str(resultados['north']))
print("Pontos mais ao sul é " + str(resultados['south']))
