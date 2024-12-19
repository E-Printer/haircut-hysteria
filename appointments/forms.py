from .models import Booking, Service
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add dynamic attributes to service choices

        self.fields['service'].widget.choices = [
            (service.id, f"{service.name}") for service in Service.objects.all()
        ]

        for service in Service.objects.all():
            self.fields['service'].widget.attrs[f'data-price-{service.id}'] = service.price
            self.fields['service'].widget.attrs[f'data-duration-{service.id}'] = service.duration