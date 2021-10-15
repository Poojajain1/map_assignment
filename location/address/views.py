#from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import googlemaps
from dotenv import load_dotenv
load_dotenv('.env')
import json
import os
# Create yo
# ur views here.

# API_KEY=os.getenv('API_KEY')
gmaps = googlemaps.Client(key=os.getenv('API_KEY', ''))

@csrf_exempt
def getGeology(request):
    if request.method=="POST":
        maps=json.loads(request.body)
        geocode_result = gmaps.geocode(maps['adr'])

        map={
            'cordinates':geocode_result[0]['geometry']['location'],
            'address':maps['adr']
        }

        #return HttpResponse(json.dumps(map))
        return HttpResponse(json.dumps(map), content_type="applicaton/xml")

