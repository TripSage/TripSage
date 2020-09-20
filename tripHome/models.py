from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.


class City(models.Model):
    cityId = models.AutoField(primary_key=True)
    cityName = models.CharField(max_length=500)


class Trip(models.Model):
    tripId = models.AutoField(primary_key=True)
    tripName = models.CharField(max_length=200)
    transportMode = [
        ("car", "Car"),
        ("bus", "Bus"),
        ("sub", "Subway"),
        ("fly", "Flight"),
    ]
    transMode = models.CharField(max_length=5, choices=transportMode)

    noPeopleTrip = models.IntegerField()
    typeTrip = [("advt", "Adventurous"), ("kd", "Kid-Friendly"),
                ("relax", "Relaxing")]
    tripType = models.CharField(max_length=10, choices=typeTrip)
    startDate = models.DateField()
    endDate = models.DateField()
    sourceCity = models.ForeignKey(City, on_delete=models.CASCADE)

    def clean(self):
        if self.endDate < self.startDate:
            raise ValidationError("Invalid Dates")
        return


class Places(models.Model):
    placeId = models.AutoField(primary_key=True)
    placeName = models.CharField(max_length=200)
    TIME_VISIT = [("mor", "Morning"), ("aft", "Afternoon"), ("eve", "Evening")]
    visitName = models.CharField(max_length=3, choices=TIME_VISIT)


class Destinations(models.Model):
    tripId = models.ForeignKey(Trip, on_delete=models.CASCADE)
    cityID = models.ForeignKey(City, on_delete=models.CASCADE)


class Contains(models.Model):
    cityID = models.ForeignKey(City, on_delete=models.CASCADE)
    placeID = models.ForeignKey(Places, on_delete=models.CASCADE)


class Tags(models.Model):
    TAG = [
        ("cv19", "Covid-19 Warning Zone"),
        ("ind", "Indoors"),
        ("pop", "Popular"),
        ("safe", "Safe Place to Visit during Covid"),
    ]
    # tags of safe and unsafe depend on population
    tagName = models.CharField(max_length=5, choices=TAG)
    tagID = models.Field(primary_key=True)


class Tagged_as(models.Model):
    placeID = models.ForeignKey(Places, on_delete=models.CASCADE)
    tagID = models.ForeignKey(Tags, on_delete=models.CASCADE)


class Visit(models.Model):
    tripId = models.ForeignKey(Trip, on_delete=models.CASCADE)
    placeID = models.ForeignKey(Places, on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField()

    def clean(self):
        if self.end < self.start:
            raise ValidationError("End time cannot be before Start")
        return
