from django.shortcuts import render

from django.views.generic import TemplateView


class FormView(TemplateView):
    template_name = 'TripSagePages/home.html'
