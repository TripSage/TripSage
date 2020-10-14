"""
url patterns for tripHome
"""
from __future__ import absolute_import
from django.urls import path
from . import views

urlpatterns = [     # pylint: disable=invalid-name
    path("", views.index, name="index"),
    path("results", views.get_response, name="postData"),
    path("search", views.results_page, name="restaurants"),
    path("charlotterelax", views.charlotterelax, name="restaurants"),
    path("charlotteadventurous", views.charlotteadventurous, name="restaurants"),
    path("charlottekidfriendly", views.charlottekidfriendly, name="restaurants"),
    
]
