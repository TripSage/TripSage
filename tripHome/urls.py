from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('results', views.getResponse, name='postData'),
    path('search', views.resultsPage, name='restaurants')
]