from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ajax/submit/', views.getResponse, name='postData'),
    path('submit/restaurants', views.getResponse, name='restaurants')
]