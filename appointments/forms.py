from .models import Booking
from django import forms

# form for user submitted bookings

class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ("stylist", "service", "message", "date", "time")
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "time": forms.DateInput(attrs={"type": "time"}),
        }