from django.contrib import admin
from .models import Booking, Stylist, Service

# Register your models here.

admin.site.register(Booking)
admin.site.register(Stylist)
admin.site.register(Service)