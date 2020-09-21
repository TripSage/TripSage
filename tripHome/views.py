"""
view for tripHome app
"""
from __future__ import absolute_import
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import xmltodict

@csrf_exempt
def get_response(request):
    """
    Function to get data from api When user click on search
    a post call is made which lands on this function
    """

    # getting the landing page data in form of dictionary
    client_data = json.loads(request.POST["requestData"])
    # getting the list of all the destinations
    location_list = client_data["destination_selected"]
    trip_kind = client_data["tripType"]  # getting trip type

    # Map for the type of the trip to the places user can visit
    type_places_map = {
        "adventurous": ["tourist_attraction", "stadium"],
        "kids": ["amusement_park", "museum"],
        "relaxing": ["art_gallery", "church", "spa"],
    }
    complete_data = set()
    final_data = {}
    for city in location_list:
        for types in trip_kind:
            for place in type_places_map[types]:
                api = (
                    "https://maps.googleapis.com/maps/api/" +
                    "place/textsearch/xml?query="
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
                selected_list = list_items[1].items()
                val = []
                for vals in selected_list:
                    val.append(vals)
                if len(val) > 1:
                    data = val[1][1]
                    complete_data = {}
                    for item in data[:6]:
                        temp_data = json.dumps(item)
                        loaded_r = json.loads(temp_data)
                        name = str(loaded_r["name"])
                        complete_data[name] = str(loaded_r["rating"])
        final_data[city] = complete_data
    return HttpResponse(json.dumps(final_data))


def results_page(request):
    """
    Function to render the results page
    """
    return render(request, "result.html", {"data": ""})


def index(request):
    """
    Function to render the main page
    """
    # Render the HTML template index.html with the data in the context variable
    return render(request, "index.html")
