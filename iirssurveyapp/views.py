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
    shphandle = ([ward for ward in fiona.open(r"C:\Users\abhis\Documents\IIRS Internship\Jupyter Lab\DDN_Geo.shp")])
    for index, ward in enumerate(shphandle):
    #    location = Point(float(longitude), float(latitude))
    #    if location.within(shape(ward['geometry'])):
    #        populationresponse = {
    #            "Ward No": ward['properties']['NUMBER1'],
    #            "Area Type": ward['properties']['TRU'],
    #            "Total People": ward['properties']['TOT_P'],
    #            "Total Males": ward['properties']['TOT_M'],
    #            "Total Females": ward['properties']['TOT_F'],
    #            "Total Literate People": ward['properties']['P_LIT'],
    #            "Total Literate Males": ward['properties']['M_LIT'],
    #            "Total Literate Females": ward['properties']['F_LIT'],
    #            "Total Illiterate People": ward['properties']['P_ILL'],
    #            "Total Illiterate Males": ward['properties']['M_ILL'],
    #            "Total Illiterate Females": ward['properties']['F_ILL'],
    #            "Total Working People": ward['properties']['TOT_WORK_P'],
    #            "Total Working Males": ward['properties']['TOT_WORK_M'],
    #            "Total Working Females": ward['properties']['TOT_WORK_F'],
    #            "Total Non Working People": ward['properties']['NON_WORK_P'],
    #            "Total Non Working Males": ward['properties']['NON_WORK_M'],
    #            "Total Non Working Females": ward['properties']['TOT_WORK_F']
    #        }
    #        return JsonResponse(populationresponse)
    #return HttpResponse("Location not inside any Ward")
            response = {
                "Soil": {
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
                },
                "Population" : {
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
                },
                "Geomorphology" : {
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
                },
                "Lithology" : {
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
                },
                "Drainage" : {
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
                },
                "Aspect" : {
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
                },
                "Slope" : {
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
            }
            return JsonResponse(response)
