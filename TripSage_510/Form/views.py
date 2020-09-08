from django.shortcuts import render, get_object_or_404

from .models import Trip, Dest, Bud

# Create your views here.
def index(request):
    trips = Trip.objects.all()