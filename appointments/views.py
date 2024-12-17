from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.db import models


class HomePage(TemplateView):
    """
    displays home page
    """
    template_name = "base.html"
