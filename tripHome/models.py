from django.db import models
from django.forms import ModelForm

# Create your models here.

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
    source_city = models.ForeignKey(City, on_delete = models.CASCADE)

    def clean(self):
        if (end < start):
            raise ValidationError('End Date cannot be before Start')
        return cleaned_data

class Places(models.Model):
    placeId = models.Field(primary=True)
    placeName = models.CharField(max_length = 200)
    timeVisit = models.DateField()

class Destinations(models.Model):
    tripId = models.ForeignKey(Trip, on_delete = models.CASCADE)
    cityID = models.ForeignKey(City, on_delete = models.CASCADE)

class Contains(models.Model):
    cityID = models.ForeignKey(City, on_delete = models.CASCADE)
    placeID = models.ForeignKey(Places, on_delete = models.CASCADE)

class Tags(models.Model):
    TAG =  [
        ('cv19': 'Covid-19 Warning Zone'),
        ('ind': 'Indoors'),
        ('pop': 'Popular'),
        ('safe': 'Safe Place to Visit during Covid')
    ]
    # tags of safe and unsafe depend on population
    tagName = models.CharField(max_length= 10, choices = TAG)
    tagID = models.Field(primary_key = True)

class Tagged_as(models.Model):
    placeID = models.ForeignKey(Places, on_delete = models.CASCADE)
    tagID = models.ForeignKey(Tags, on_delete = models.CASCADE)

class Visit(models.Model):
    tripId = models.ForeignKey(Trip, on_delete = models.CASCADE)
    placeID = models.ForeignKey(Places, on_delete = models.CASCADE)
    start = models.DateField()
    end = models.DateField()

    def clean(self):
        if (end < start):
            raise ValidationError('End time cannot be before Start')
        return cleaned_data

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['cityId', 'cityName']

class TripForm(ModelForm):
    class Meta:
        model = Trip
        fields = ['tripId', 'tripName', 'tran', 'no_people', 'tripType', 'start', 'end']

