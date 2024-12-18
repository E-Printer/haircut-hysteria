from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('services', views.Services.as_view(), name='services'),
    path('make-booking/', views.make_booking, name='make_booking'),
    path('edit-booking/<int:pk>', views.edit_booking, name='edit_booking'),
    path('delete-booking/<int:pk>', views.delete_booking, name='delete_booking'),
    path('booking-list/', views.BookingList.as_view(), name='booking_list'),
]