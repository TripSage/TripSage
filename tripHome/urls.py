from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ajax/submit/', views.postData, name='postData'),
    path('submit/restaurants', views.getResponse, name='restaurants')
]