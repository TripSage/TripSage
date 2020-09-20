import xmltodict
from django.shortcuts import render
from .models import Trip
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import xml.etree.ElementTree as ET
import requests
import json
from json import dumps, loads, JSONEncoder, JSONDecoder


#############################
# Function to get data from api
# When user click on search, a
# post call is made which lands
# on this function
#############################
@csrf_exempt
def getResponse(request):
    # getting the landing page data in form of dictionary
    clientData = json.loads(request.POST["requestData"])
    # getting the list of all the destinations
    location_list = clientData["destination_selected"]
    trip_kind = clientData["tripType"]  # getting trip type

    # Map for the type of the trip to the places user can visit
    type_places_map = {
        "adventurous": ["tourist_attraction", "stadium"],
        "kids": ["amusement_park", "museum"],
        "relaxing": ["art_gallery", "church", "spa"],
    }
    # save data by user
    # change response url
    # multiple response
    # create dictionary
    # final zip of data is created here
    complete_data = set()
    final_data = {}
    for city in location_list:
        for type in trip_kind:
            for place in type_places_map[type]:
                api = (
                    "https://maps.googleapis.com/maps/api/place/textsearch/xml?query="
                    + place
                    + "+in+"
                    + city
                    + "&key=AIzaSyAIsboWfXVchmgBxPGKG5lUF9AENUKcSI8"
                )
                response = requests.get(api)
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
                if len(val) > 1:
                    data = val[1][1]
                    complete_data = {}
                    for item in data[:6]:
                        r = json.dumps(item)
                        loaded_r = json.loads(r)
                        # complete_data.add((str(loaded_r["name"]), str(loaded_r["rating"])))
                        complete_data[str(loaded_r["name"])] = str(loaded_r["rating"])
        final_data[city] = complete_data
    return HttpResponse(json.dumps(final_data))


#############################
# Function to render the results page
#############################
def resultsPage(request):
    return render(request, "result.html", {"data": ""})


#############################
# Function to render the main page
#############################
def index(request):
    # Render the HTML template index.html with the data in the context variable
    return render(request, "index.html")
