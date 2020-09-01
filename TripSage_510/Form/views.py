from django.shortcuts import render, get_object_or_404

from .models import Trip, Dest, Bud

# Create your views here.
def index(request, trips_id):
    trips = Trip.objects.all()
    trip = get_object_or_404(Trip, pk = trips_id)
    #context = {"trips":  trips}
    return render(request, 'Form/index.html',{"trips":  trip})

def display(request, trips_id):

    trips = get_object_or_404(Trip, pk = trips_id)
    return render(request, 'Form/display.html', {"trips":  trips})