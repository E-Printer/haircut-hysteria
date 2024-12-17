from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('make-booking/', views.make_booking, name='make_booking'),
]