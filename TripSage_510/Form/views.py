from django.shortcuts import render, get_object_or_404
from Form.forms import SelectTrip
from django.http import HttpResponseRedirect
from .models import Trip, Dest, Bud
import datetime

from django.urls import reverse

# Create your views here.
def index(request, pk):
    #trips = Trip.objects.all()
    trip = get_object_or_404(Trip, pk = pk)
    if request.method == 'POST':
        # populate instance with data from POST request: binding (allows to validate form)
        form = SelectTrip(request.POST)
        if form.is_valid():
            trip.end_date = form.cleaned_data['end_date']
            trip.start_date = SelectTrip.start_date
            trip.trip_type = SelectTrip.trip_type
            trip.save()

            return HttpResponseRedirect(reverse('index') )
        else:
            # if GET or other method:
            start_date = datetime.date.today()
            end_date = datetime.date.today() + datetime.timedelta(weeks=3)
            trip_type = 'Adventurous'
            form = SelectTrip(initial = {'start_date': start_date,
                                'end_date': end_date,
                                'trip_type': trip_type})

        context = {
            'form': form,
            'trip': trip
        }

    #context = {"trips":  trips}
    return render(request, 'Form/index.html',context)

def display(request, trips_id):

    trips = get_object_or_404(Trip, pk = trips_id)
    return render(request, 'Form/display.html', {"trips":  trips})