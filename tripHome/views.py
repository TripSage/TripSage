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
    print(root)
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
    return render(request, 'result.html', {'data': new_data})


def index(request):

    if request.is_ajax():
        #do something
        request_data = request.POST
        return HttpResponse("OK")

    """View function for home page of site."""
    # trip_type = request.POST.get('trip_type', 'None')
    # try:
    #     transp = request.POST['transp']
    #     no_people = request.POST['no_people']
    #     start = request.POST['start_date']
    #     end = request.POST['end_date']
    #     source_city = request.POST['soource_city']

    # except (KeyError, Trip.DoesNotExist):
    #     #return render(request)
    #     return None


    # #if request.method == 'POST':

    # #trips_list = Trip.objects.orderby('-tripId')[:10]
    # context = {'trip_type': trip_type,
    #             'transp': transp,
    #             'no_people': no_people,
    #             'start': start,
    #             'end': end,
    #             'source_city': source_city}
    # Generate counts of some of the main objects
    num_books = 5
    num_instances = 5
    
    # Available books (status = 'a')
    num_instances_available = 5
    
    # The 'all()' is implied by default.    
    num_authors = 5
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


    # return render(request, 'tripHome/index.html')
