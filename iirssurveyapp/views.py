from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.gis.geos import GEOSGeometry
from .models import Userloclayer
from django.http import JsonResponse
from shapely.geometry import MultiPolygon, mapping, Point, Polygon, shape
from shapely.geometry.polygon import Polygon
import fiona
import json

# Create your views here.

def index(request):
    return HttpResponse("IIRS Survey App")

def getlocation(request, latitude, longitude, layer):
    point = {
        "type": "Point",
        "coordinates": [float(longitude), float(latitude)]
    }
    loclayer = Userloclayer.objects.create(location = GEOSGeometry(json.dumps(point)), layer = layer)
    loclayer.save()
    if layer == "population":
        shphandle = ([ward for ward in fiona.open(r"C:\Users\abhis\Documents\IIRS Internship\Jupyter Lab\DDN_Geo.shp")])
        for index, ward in enumerate(shphandle):
            location = Point(float(longitude), float(latitude))
            if location.within(shape(ward['geometry'])):
                populationrespone = {
                    "Ward No": ward['properties']['NUMBER1'],
                    "Area Type": ward['properties']['TRU'],
                    "Total People": ward['properties']['TOT_P'],
                    "Total Males": ward['properties']['TOT_M'],
                    "Total Females": ward['properties']['TOT_F'],
                    "Total Literate People": ward['properties']['P_LIT'],
                    "Total Literate Males": ward['properties']['M_LIT'],
                    "Total Literate Females": ward['properties']['F_LIT'],
                    "Total Illiterate People": ward['properties']['P_ILL'],
                    "Total Illiterate Males": ward['properties']['M_ILL'],
                    "Total Illiterate Females": ward['properties']['F_ILL'],
                    "Total Working People": ward['properties']['TOT_WORK_P'],
                    "Total Working Males": ward['properties']['TOT_WORK_M'],
                    "Total Working Females": ward['properties']['TOT_WORK_F'],
                    "Total Non Working People": ward['properties']['NON_WORK_P'],
                    "Total Non Working Males": ward['properties']['NON_WORK_M'],
                    "Total Non Working Females": ward['properties']['TOT_WORK_F']
                }
                return JsonResponse(populationrespone)
        return HttpResponse("Location not inside any Ward")

    if layer == "soil":
        shphandle = ([ward for ward in fiona.open(r"C:\Users\abhis\Documents\IIRS Internship\Jupyter Lab\DDN_Geo.shp")])
        for index, ward in enumerate(shphandle):
            location = Point(float(longitude), float(latitude))
            if location.within(shape(ward['geometry'])):
                soilrespone = {
                    "Ward No": ward['properties']['NUMBER1']
                }
                return JsonResponse(soilrespone)
        return HttpResponse("Location not inside any Ward")

    if layer == "drainage":
        shphandle = ([ward for ward in fiona.open(r"C:\Users\abhis\Documents\IIRS Internship\Jupyter Lab\DDN_Geo.shp")])
        for index, ward in enumerate(shphandle):
            location = Point(float(longitude), float(latitude))
            if location.within(shape(ward['geometry'])):
                drainagerespone = {
                    "Ward No": ward['properties']['NUMBER1']
                }
                return JsonResponse(drainagerespone)
        return HttpResponse("Location not inside any Ward")

    if layer == "lithology":
        shphandle = ([ward for ward in fiona.open(r"C:\Users\abhis\Documents\IIRS Internship\Jupyter Lab\DDN_Geo.shp")])
        for index, ward in enumerate(shphandle):
            location = Point(float(longitude), float(latitude))
            if location.within(shape(ward['geometry'])):
                lithologyrespone = {
                    "Ward No": ward['properties']['NUMBER1']
                }
                return JsonResponse(lithologyrespone)
        return HttpResponse("Location not inside any Ward")

    if layer == "geomorphology":
        shphandle = ([ward for ward in fiona.open(r"C:\Users\abhis\Documents\IIRS Internship\Jupyter Lab\DDN_Geo.shp")])
        for index, ward in enumerate(shphandle):
            location = Point(float(longitude), float(latitude))
            if location.within(shape(ward['geometry'])):
                geomorphorespone = {
                    "Ward No": ward['properties']['NUMBER1']
                }
                return JsonResponse(geomorphorespone)
        return HttpResponse("Location not inside any Ward")
