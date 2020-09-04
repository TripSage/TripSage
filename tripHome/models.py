from django.db import models
from django.forms import ModelForm

# Create your models here.

# FILE I'LL BE WORKING IN PRIMARILY
class City(models.Model):
    cityId = models.Field(primary_key = True)
    cityName = models.CharField(max_length = 500)

class Trip(models.Model):
    tripId = models.Field(primary_key = True)
    tripName = models.CharField(max_length = 200)
    TRANSP = [
        ('car', 'Car'),
        ('bus', 'bus'),
        ('sub', 'Subway')
    ]
    tran = models.CharField(max_length = 5, choices = TRANSP)

    no_people = models.IntegerField()
    TYPE_TRIP = [
        ('advt': 'Adventurous'),
        ('kd': 'Kid-Friendly'),
        ('relax': 'Relaxing')
    ]
    tripType = models.CharField(max_length= 10, choices = TYPE_TRIP)
    start = models.DateField()
    end = models.DateField()

    def clean(self):
        if (end < start):
            raise ValidationError('End Date cannot be before Start')
        return cleaned_data

class Places(models.Model):
    placeId = models.Field(primary=True)
    placeName = models.CharField(max_length = 200)
    timeVisit = models.DaetField()

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['cityId', 'cityName']

class TripForm(ModelForm):
    class Meta:
        model = Trip
        fields = ['tripId', 'tripName', 'tran', 'no_people', 'tripType', 'start', 'end']

