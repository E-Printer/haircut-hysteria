from django.shortcuts import render, get_object_or_404, redirect
from .forms import BookingForm
from .models import Booking
from django.views.generic import TemplateView, ListView
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import models


class HomePage(TemplateView):
    """
    displays home page
    """
    template_name = "base.html"

class BookingList(ListView):
    """
    view all a users bookings as a list
    """
    model = Booking
    template_name = "my_bookings.html"
    context_object_name = "bookings"

    def get_queryset(self):
        return Booking.objects.filter(customer=self.request.user)

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
            messages.success(request, "Your booking is pending")
            return redirect("home")
        else:
            messages.error(request, "There was an error making your appointment")
    else:
        form = BookingForm()

    return render(request, "new_booking.html", {"form": form})

# view for deleting a booking

def edit_booking(request,  pk):
    """
    Take an instance of a booking based on it's id and edit it
    """
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            booking = form.save()
            messages.success(request, "Appointment updated successfully!")
            return redirect('booking_list')
        else: messages.error(request, "There was an error updating your appointment")
    else:
        form = BookingForm(instance=booking)
    return render(request, 'edit_booking.html', {
        'form': form,
        'booking': booking
    })


def delete_booking(request):
    """
    Take an instance of a booking based on it's id and delete it
    """

