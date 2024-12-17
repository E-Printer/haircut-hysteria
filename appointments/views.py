from django.shortcuts import render, redirect
from .forms import BookingForm
from django.views.generic import TemplateView
from django.contrib import messages

class HomePage(TemplateView):
    """
    displays home page
    """
    template_name = "base.html"

# view for making a booking

def make_booking(request):
    """
    Create an instance of a booking
    """
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.customer = request.user
            booking.save()
            messages.success(request, "Your booking is pending")#]
            return redirect("home")
        else:
            messages.error(request, "There was an error making your appointment")
    else:
        form = BookingForm()

    return render(request, "new_booking.html", {"form": form})