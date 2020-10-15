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


# Map for the type of the trip to the places user can visit
TYPES_PLACE_MAP = {
    "adventurous": ["tourist_attraction", "stadium"],
    "kids": ["amusement_park", "museum"],
    "relaxing": ["art_gallery", "church", "spa"],
}

@csrf_exempt
def get_response(request):
    """
    Function to get data from api When user click on search
    a post call is made which lands on this function
    """
    # getting the landing page data in form of dictionary
    client_data = json.loads(request.POST["requestData"])
    final_data = {}
    
    for city in client_data["destination_selected"]:
        complete_data = {}
        for types in client_data["tripType"]:
            for place in TYPES_PLACE_MAP[types]:
                api = (
                    "https://maps.googleapis.com/maps/api/" +
                    "place/textsearch/xml?query="
                    + place
                    + "+in+"
                    + city
                    + "&key=AIzaSyAIsboWfXVchmgBxPGKG5lUF9AENUKcSI8"
                )
                data_dict = xmltodict.parse(requests.get(api).content)
                results = json.loads(json.dumps(data_dict))
                list_items = []
                for item in results.items():
                    list_items = item
                val = []
                for values in list_items[1].items():
                    val.append(values)
                if len(val) > 1:
                    for values in val[1][1][:3]:
                        loaded_r = json.loads(json.dumps(values))
                        complete_data[str(loaded_r["name"])] = str(loaded_r["rating"])
        final_data[city] = complete_data
    return HttpResponse(json.dumps(final_data))


def results_page(request):
    """
    Function to render the results page
    """
    return render(request, "charlotterelax.html", {"data": ""})


def index(request):
    """
    Function to render the main page
    """
    # Render the HTML template index.html with the data in the context variable
    return render(request, "index.html")

def charlotterelax(request):
    """
    Function to render the results page
    """
    return render(request, "charlotterelax.html")

def charlotteadventurous(request):
    """
    Function to render the results page
    """
    return render(request, "charlotteadventurous.html")

def charlottekidfriendly(request):
    """
    Function to render the results page
    """
    return render(request, "charlottekidfriendly.html")

def raleighrelax(request):
    """
    Function to render the results page
    """
    return render(request, "raleighrelax.html")

def raleighadventurous(request):
    """
    Function to render the results page
    """
    return render(request, "raleighadventurous.html")

def raleighkidfriendly(request):
    """
    Function to render the results page
    """
    return render(request, "raleighkidfriendly.html")


#adding tests
def increment(a):
    a = a +1
    return a

def add(a,b):
    c = a + b
    return c

def subtract(a,b):
    c = a-b
    return c

def multiply(a,b):
    c = a*b
    return c

def divide(a,b):
    c = a/b
    return c

def modulo(a,b):
    c = a%b
    return c



def test_increment_method():
    test_val = increment(1)
    assert test_val == 2
    
def test_add_method():
    test_val = add(1,2)
    assert test_val == 3

def test_subtract_method():
    test_val = subtract(1,1)
    assert test_val == 0

def test_multiply_method():
    test_val = multiply(1,2)
    assert test_val == 2

def test_divide_method():
    test_val = divide(4,2)
    assert test_val == 2

def test_modulo_method():
    test_val = modulo(2,2)
    assert test_val == 0
