

uri = "file:///Users/your/path/here/Earthquakes/data/EQ_search.csv?type=csv&xField=longitude&yField=latitude&spatialIndex=no&subsetIndex=no&watchFile=no&crs=epsg:32610"

layer = QgsVectorLayer(uri, 'EQ', "delimitedtext")

QgsProject.instance().addMapLayer(layer)

## To add beachball symbology

features = layer.getFeatures()

categories = []

for feature in features:

    # initialize the default symbol for this geometry type
    symbol = QgsSymbol.defaultSymbol(layer.geometryType())
    
    # configure a symbol layer
    symbol_layer = QgsSvgMarkerSymbolLayer('/your/path/here/Earthquakes/data/bbs/svg/%s' % feature['id'] +'.svg', size=feature['magnitude']*2)

    # replace default symbol layer with the configured one
    if symbol_layer is not None:
        symbol.changeSymbolLayer(0, symbol_layer)
    
    # remove markers for data without focal mechanisms by setting opacity
    if feature['nc_np1_strike'] == NULL:
        symbol.setOpacity(0)
#    elif feature['magnitude'] <3:
#        symbol.setOpacity(0)

    # create renderer object
    category = QgsRendererCategory(feature['id'], symbol, str(feature['id']))
    # entry for the list of category items
    categories.append(category)
    

# create renderer object
renderer = QgsCategorizedSymbolRenderer('id', categories)

# assign the created renderer to the layer
if renderer is not None:
    layer.setRenderer(renderer)

layer.triggerRepaint()




