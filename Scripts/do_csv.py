input = [
    ['Atut Łódź', 51.737189, 19.384456, 'http://www.propertynews.pl/retail-map/obiekt,atut-lodz,310.html'],
['Carrefour Łódź Bałuty', 51.804472, 19.380197, 'http://www.propertynews.pl/retail-map/obiekt,carrefour-lodz-baluty,851.html'],
['Carrefour Łódź Bandurskiego', 51.752696, 19.420098, 'http://www.propertynews.pl/retail-map/obiekt,carrefour-lodz-bandurskiego,856.html'],
['Carrefour Łódź Przybyszewskiego', 51.751828, 19.503265, 'http://www.propertynews.pl/retail-map/obiekt,carrefour-lodz-przybyszewskiego,845.html'],
['Centrum Handlowe Guliwer', 51.71045, 19.49216, 'http://www.propertynews.pl/retail-map/obiekt,centrum-handlowe-guliwer,229.html'],
['Centrum Handlowe M1 Łódź', 51.793436, 19.510298, 'http://www.propertynews.pl/retail-map/obiekt,centrum-handlowe-m1-lodz,32.html'],
['Centrum Handlowe Pasaż Łódzki', 51.749777, 19.441552, 'http://www.propertynews.pl/retail-map/obiekt,centrum-handlowe-pasaz-lodzki,34.html'],
['Centrum Handlowe Tulipan', 51.765252, 19.49554, 'http://www.propertynews.pl/retail-map/obiekt,centrum-handlowe-tulipan,35.html'],
['CH Sukcesja', 51.750009, 19.448306, 'http://www.propertynews.pl/retail-map/obiekt,ch-sukcesja,207.html'],
['Galeria Łódzka', 51.758997, 19.465279, 'http://www.propertynews.pl/retail-map/obiekt,galeria-lodzka,33.html'],
['Galeria Retkińska', 51.746402, 19.397149, 'http://www.propertynews.pl/retail-map/obiekt,galeria-retkinska,544.html'],
['Manufaktura', 51.779755, 19.446722, 'http://www.propertynews.pl/retail-map/obiekt,manufaktura,13.html'],
['Port Łódź', 51.703741, 19.415173, 'http://www.propertynews.pl/retail-map/obiekt,port-lodz,31.html'],
['Skwer Handlowy Łódź', 51.742899, 19.385544, 'http://www.propertynews.pl/retail-map/obiekt,skwer-handlowy-lodz,425.html'],
['Street Mall Vis à Vis', 51.817413, 19.435454, 'http://www.propertynews.pl/retail-map/obiekt,street-mall-vis-vis,688.html'],
['Tesco Łódź', 51.760614, 19.519803, 'http://www.propertynews.pl/retail-map/obiekt,tesco-lodz,744.html']
]

print("X,Y,id,nazwa")
for galeria in input:
    print("{},{},'{}',{}".format(galeria[1], galeria[2], input.index(galeria), galeria[0]))