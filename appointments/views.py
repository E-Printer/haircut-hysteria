from django.shortcuts import render
from django.views.generic import TemplateView

class HomePage(TemplateView):
    """
    displays home page
    """
    template_name = "index.html"


