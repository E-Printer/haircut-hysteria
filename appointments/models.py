from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Service(models.Model):
    """
    """
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    duration = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=00.00)

    def __str__(self):
        return f"You have booked {self.name}."

class Stylist(models.Model):
    """
    """
    name = models.CharField(max_length=150, unique=True)
    type = models.CharField(max_length=50)
    bio = models.TextField(blank=True, null=True, help_text="A short bio")

    def __str__(self):
        return f"Your stylist is {self.name}."

STATUS = ((0, "Pending"), (1, "Confirmed"), (2, "Cancelled"))

class Booking(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    stylist = models.ForeignKey(Stylist, on_delete=models.CASCADE, related_name="appointments")
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    message = models.CharField(max_length=1000, blank=True, null=True)
    date = models.DateField()
    time = models.TimeField()
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Booking for {self.customer}, with {self.stylist} at {self.time} on {self.date}."
