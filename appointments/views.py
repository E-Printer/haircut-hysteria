from django.shortcuts import render, get_object_or_404, redirect
from .forms import BookingForm
from .models import Booking
from django.views.generic import TemplateView, ListView
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings


class HomePage(TemplateView):
    """
    displays home page
    """
    template_name = "index.html"

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

@login_required
def make_booking(request):
    """
    Create an instance of a booking and send a confirmation email.
    """
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)  # Save but do not commit to set the customer
            booking.customer = request.user  # Set the customer from the logged-in user
            booking.save()
            send_confirmation_email(booking)
            messages.success(request, "Your booking has been successfully created and a confirmation email has been sent!")
            return redirect("home")
        else:
            messages.error(request, "There was an error making your appointment. Please check the form and try again.")
    else:
        form = BookingForm()

    return render(request, "new_booking.html", {"form": form})

def send_confirmation_email(booking):
    subject = "Booking Confirmation"
    message = (
        f"Dear {booking.customer},\n\n"
        f"Your booking has been successfully confirmed, here are the details:\n\n"
        f"{booking.stylist}\n\n"
        f"{booking.service}\n\n" 
        f"Date and time: {booking.date} at {booking.time}\n\n" 
        f"Message from you: {booking.message if booking.message else 'No additional message'}\n\n"
        f"Thank you for choosing our service!\n\n"
        f"Best regards,\n"
        f"The Haircut Hysteria Team"
    )
    recipient_email = booking.customer.email  # Use the email associated with the user
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [recipient_email],
        fail_silently=False,
    )


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

def delete_booking(request, pk):
    """
    Take an instance of a booking based on it's id and delete it
    """
    booking = get_object_or_404(Booking, pk=pk)
    booking.delete()
    messages.success(request, "Post deleted successfully!")
    return redirect('booking_list')

