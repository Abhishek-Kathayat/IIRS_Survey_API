from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.gis.geos import GEOSGeometry
from .models import Userloclayer, Layer
from django.http import JsonResponse
from shapely.geometry import MultiPolygon, mapping, Point, Polygon, shape
from shapely.geometry.polygon import Polygon
from django.core import serializers
import fiona
import json
import os
import fnmatch
import geopandas


def index(request):
    return HttpResponse("IIRS Survey App")

def getLayers(request):
    layers = Layer.objects.all()
    layerresponse = [
        {
            'layer': str(layer)
        }
        for layer in list(layers)
    ]
    return JsonResponse(layerresponse, safe=False)

def getlocation(request, latitude, longitude):
    point = {
        "type": "Point",
        "coordinates": [float(longitude), float(latitude)]
    }
    loclayer = Userloclayer.objects.create(location = GEOSGeometry(json.dumps(point)))
    loclayer.save()

    responsedata = {}
    shapefiles = list()
    for file_name in os.listdir('C:/Users/abhis/Documents/IIRS Internship/Jupyter Lab/ShapeFiles/Modified ShapeFiles/'):
        if fnmatch.fnmatch(file_name, '*.shp'):
            shapefiles.append(file_name)

    for shapefile in shapefiles:
        filehandle = geopandas.read_file('C:/Users/abhis/Documents/IIRS Internship/Jupyter Lab/ShapeFiles/Modified ShapeFiles/' + shapefile)
        file_crs = filehandle.crs
        if(file_crs['init'] != 'epsg:4326'):
            filehandle = filehandle.to_crs({'init': 'epsg:4326'})
            filehandle.to_file('C:/Users/abhis/Documents/IIRS Internship/Jupyter Lab/ShapeFiles/Modified ShapeFiles/Temp_data.shp')
        else:
            filehandle.to_file('C:/Users/abhis/Documents/IIRS Internship/Jupyter Lab/ShapeFiles/Modified ShapeFiles/Temp_data.shp')

        response = getShpData(shapefile, latitude, longitude)

        if shapefile == 'Drainage.shp':
            responsedata["Drainage"] = response
        elif shapefile == 'DDN_Geo.shp':
            responsedata["Population"] = response
        elif shapefile == 'Geomorphology.shp':
            responsedata["Geomorphology"] = response
        elif shapefile == 'Lithology.shp':
            responsedata["Lithology"] = response
        elif shapefile == 'Existing_Site.shp':
            responsedata["Existing Site"] = response
        elif shapefile == 'Slope.shp':
            responsedata["Slope"] = response
        elif shapefile == 'Soil.shp':
            responsedata["Soil"] = response
        elif shapefile == 'LULC_12Classes.shp':
            responsedata["Land Usage"] = response

    return JsonResponse(responsedata)


def getShpData(shapefile, latitude, longitude):
    shphandle = ([ward for ward in fiona.open(r"C:\Users\abhis\Documents\IIRS Internship\Jupyter Lab\ShapeFiles\Modified ShapeFiles\Temp_data.shp")])
    for index, ward in enumerate(shphandle):
        location = Point(float(longitude), float(latitude))
        if location.within(shape(ward['geometry'])):
            if shapefile == 'Drainage.shp':
                drainage = {
                }
                return drainage
            elif shapefile == 'DDN_Geo.shp':
                population = {
                    "Total People": ward['properties']['TOT_P'],
                    "Total Males": ward['properties']['TOT_M'],
                    "Total Females": ward['properties']['TOT_F'],
                    "Total Literate People": ward['properties']['P_LIT'],
                    "Total Illiterate People": ward['properties']['P_ILL'],
                    "Total Working People": ward['properties']['TOT_WORK_P'],
                    "Total Non Working People": ward['properties']['NON_WORK_P']
                }
                return population
            elif shapefile == 'Geomorphology.shp':
                geomorphology = {
                    "Geomorphology Class": ward['properties']['GEOM_CLASS'],
                    "Regional": ward['properties']['REGIONAL_1'],
                    "Regional": ward['properties']['REGIONAL_G']
                }
                return geomorphology
            elif shapefile == 'Lithology.shp':
                lithology = {
                    "Geology": ward['properties']['GEOLOGY_'],
                    "Geology ID": ward['properties']['GEOLOGY_ID'],
                    "Lithology": ward['properties']['LITHOLOGY']
                }
                return lithology
            elif shapefile == 'Existing_Site.shp':
                existing_site = {
                }
                return existing_site
            elif shapefile == 'Slope.shp':
                slope = {
                    "Slope Degree": ward['properties']['slope_degr']
                }
                return slope
            elif shapefile == 'Soil.shp':
                soil = {
                    "Soil Code": ward['properties']['SO_CODE'],
                    "Soil Type": ward['properties']['SOIL_TYPE'],
                    "Soil Depth": ward['properties']['SoilDepth'],
                    "Soil Erosion": ward['properties']['SoilErosio'],
                    "Soil Texture": ward['properties']['SoilTextur'],
                }
                return soil
            elif shapefile == 'LULC_12Classes.shp':
                lulc_class = {
                    "Land Usage Class": ward['properties']['lu_class'],
                    "Land Usage": ward['properties']['r1_lulc'],
                }
                return lulc_class

    if shapefile == 'Drainage.shp':
        drainage = {}
        return drainage
    elif shapefile == 'DDN_Geo.shp':
        population = {}
        return population
    elif shapefile == 'Geomorphology.shp':
        geomorphology = {}
        return geomorphology
    elif shapefile == 'Lithology.shp':
        lithology = {}
        return lithology
    elif shapefile == 'Existing_Site.shp':
        existing_site = {}
        return existing_site
    elif shapefile == 'Slope.shp':
        slope = {}
        return slope
    elif shapefile == 'Soil.shp':
        soil = {}
        return soil
    elif shapefile == 'LULC_12Classes.shp':
        lulc_class = {}
        return lulc_class




#elif shapefile in ['Hospitals.shp', 'Institutions.shp', 'MajorCityPoints.shp', 'OSM_Infra.shp', 'OSM_Points.shp']:
#    loc_file = ward['geometry']
#    wardhandle = ([wardloc for wardloc in fiona.open(r"C:\Users\abhis\Documents\IIRS Internship\Jupyter Lab\ShapeFiles\Modified ShapeFiles\DDN_Geo.shp")])
#    for index, wardloc in enumerate(wardhandle):
#        if location.within(shape(wardloc['geometry'])) and loc_file.within(shape(wardloc['geometry'])):
#            if shapefile is 'Hospital.shp':
#                hospital = {
#                    "FID_Hospital": ward['properties']['FID_HOSPIT'],
#                    "Hospital Name": ward['properties']['NAME'],
#                    "FID_Municipality": ward['properties']['FID_MUNICI'],
#                    "Area Type": ward['properties']['TRU']
#                }
#                break
#            elif shapefile is 'Institutions.shp':
#                institutions = {
#                    "FID_Institute": ward['properties']['FID_INSTIT'],
#                    "Institute Name": ward['properties']['Name'],
#                    "Nearby Place": ward['properties']['nearby_pla'],
#                    "Area Type": ward['properties']['TRU'],
#                    "FID_MUNICI": ward['properties']['FID_MUNICI']
#                }
#                break
#            elif shapefile is 'MajorCityPoints.shp':
#                majorcitypoints =  {
#                    "ID": ward['properties']['Id'],
#                    "Grid Code": ward['properties']['grid_code'],
#                    "Original FID": ward['properties']['ORIG_FID']
#                }
#                break
#            elif shapefile is 'OSM_Infra.shp':
#                osm_infra = {
#                    "Name": ward['properties']['ONGC Telbhawan'],
#                    "Amenity": ward['properties']['public_building']
#                }
#                break
