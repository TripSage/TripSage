from django.urls import path
from . import views

app_name = 'Form'
urlpatterns = [
    path("", views.index, name = "index"),
    #path('<int:trips_id>/', views.display, name = 'display')
]