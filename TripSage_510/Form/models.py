from django.db import models
import uuid
#import datetime


# Create your models here.
class Trip(models.Model):
    trip_type = models.CharField(max_length = 100)
    start = models.DateField()
    end = models.DateField()
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, 
        #help_text='Unique ID for this trip')


class Dest(models.Model):
    city = models.CharField(max_length = 200)

class Bud(models.Model):
    budget = models.FloatField()