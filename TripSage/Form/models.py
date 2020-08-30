from django.db import models
#import datetime


# Create your models here.
class Trip(models.Model):
    trip_type = models.CharField(max_length = 100)

class Dest(models.Model):
    city = models.CharField(max_length = 200)

class Bud(models.Model):
    budget = models.FloatField()