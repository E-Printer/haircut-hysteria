from .models import Booking
from django import forms
from django.core.mail import send_mail

# form for user submitted bookings

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ("stylist", "service", "message", "date", "time")
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "time": forms.TimeInput(attrs={"type": "time"}),
        }