from django.forms import ModelForm
from . import models

# Creating a form for the models and constraints

class CityForm(ModelForm):
    class Meta:
        model = models.City
        fields = ['cityId', 'cityName']

class TripForm(ModelForm):
    class Meta:
        modelT = models.Trip
        modelP = models.Places
        fields = ['tripId', 'tripName', 'transMode', 'noPeopleTrip', 'tripType', 'startDate', 'endDate', 'placeName']

# TO DO: create forms and validation for PlaceID vs TripID 