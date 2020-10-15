"""
view for tripHome app
"""
from __future__ import absolute_import
import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
import requests
import xmltodict

# method for signing up the user
def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'registration/signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})

# Map for the type of the trip to the places user can visit
TYPES_PLACE_MAP = {
    "adventurous": ["tourist_attraction", "stadium"],
    "kids": ["amusement_park", "museum"],
    "relaxing": ["art_gallery", "church", "spa"],
}

# method for log in of the user
def signin(request):
    if request.user.is_authenticated:
        return render(request, '/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'registration/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})

# method for logout of the user
def signout(request):
    logout(request)
    return redirect('/')


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
def increment(arg_one):
    """
    Function to increment
    """
    arg_one = arg_one+1
    return arg_one

def add(arg_one,arg_two):
    """
    Function to add
    """
    ans = arg_one + arg_two
    return ans

def subtract(arg_one,arg_two):
    """
    Function to subtract
    """
    ans = arg_one - arg_two
    return ans

def multiply(arg_one,arg_two):
    """
    Function to multiply
    """
    ans = arg_one * arg_two
    return ans

def divide(arg_one,arg_two):
    """
    Function to divide
    """
    ans = arg_one/arg_two
    return ans

def modulo(arg_one,arg_two):
    """
    Function to modulo
    """
    ans = arg_one%arg_two
    return ans



def test_increment_method():
    """
    Function to check increment
    """
    test_val = increment(1)
    assert test_val == 2

def test_add_method():
    """
    Function to check add
    """
    test_val = add(1,2)
    assert test_val == 3

def test_subtract_method():
    """
    Function to check subtract
    """
    test_val = subtract(1,1)
    assert test_val == 0

def test_multiply_method():
    """
    Function to check multiply
    """
    test_val = multiply(1,2)
    assert test_val == 2

def test_divide_method():
    """
    Function to check divide
    """
    test_val = divide(4,2)
    assert test_val == 2

def test_modulo_method():
    """
    Function to check modulo
    """
    test_val = modulo(2,2)
    assert test_val == 0
