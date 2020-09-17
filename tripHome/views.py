import xmltodict
from django.shortcuts import render
from . models import Trip
from . forms import TripForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import xml.etree.ElementTree as ET
import requests
import json

@csrf_exempt
def getResponse(request):
    clientData = json.loads(request.POST['requestData'])
    response = requests.get("https://maps.googleapis.com/maps/api/place/textsearch/xml?query=restaurants+in+Raleigh"
                            "&key=AIzaSyAIsboWfXVchmgBxPGKG5lUF9AENUKcSI8")
    root = ET.fromstring(response.content)
    root = ET.fromstring(response.content)
    data_dict = xmltodict.parse(response.content)
    json_data = json.dumps(data_dict)
    results = json.loads(json_data)
    values = results.items()
    list_items = []
    for item in values:
        list_items = item
    a = list_items[1].items()
    val = []
    for b in a:
        val.append(b)
    data = val[1][1]
    items_name = []
    items_rating = []
    for item in data:
        r = json.dumps(item)
        loaded_r = json.loads(r)
        items_name.append(loaded_r['name'])
        items_rating.append(loaded_r['rating'])

    new_data = zip(items_name, items_rating)
    return HttpResponse(new_data)

def resultsPage(request):
    return render(request, 'result.html', {'data': ""})

def index(request):

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')


    # return render(request, 'tripHome/index.html')
