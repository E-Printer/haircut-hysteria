from django.test import TestCase
from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from decimal import Decimal
from datetime import datetime, date, time
from .models import Service, Stylist, Booking 


# Create your tests here.

class ServiceModelTest(TestCase):
    def setUp(self):
        self.service = Service.objects.create(
            name="Haircut",
            description="Basic haircut service",
            duration=30,
            price=25.00
        )

    def test_service_creation(self):
        self.assertTrue(isinstance(self.service, Service))
        self.assertEqual(str(self.service), "Haircut")

    def test_service_fields(self):
        self.assertEqual(self.service.name, "Haircut")
        self.assertEqual(self.service.description, "Basic haircut service")
        self.assertEqual(self.service.duration, 30)
        self.assertEqual(self.service.price, Decimal('25.00'))

    def test_unique_name_constraint(self):
        duplicate_service = Service(
            name="Haircut",
            description="Another haircut service",
            duration=45,
            price=30.00
        )
        with self.assertRaises(ValidationError):
            duplicate_service.full_clean()

class StylistModelTest(TestCase):
    def setUp(self):
        self.stylist = Stylist.objects.create(
            name="John Doe",
            type="Senior",
            bio="Experienced hairstylist with 10 years of experience"
        )

    def test_stylist_creation(self):
        self.assertTrue(isinstance(self.stylist, Stylist))
        self.assertEqual(str(self.stylist), "John Doe")

    def test_stylist_fields(self):
        self.assertEqual(self.stylist.name, "John Doe")
        self.assertEqual(self.stylist.type, "Senior")
        self.assertEqual(
            self.stylist.bio,
            "Experienced hairstylist with 10 years of experience"
        )

    def test_unique_name_constraint(self):
        duplicate_stylist = Stylist(
            name="John Doe",
            type="Junior"
        )
        with self.assertRaises(ValidationError):
            duplicate_stylist.full_clean()

class BookingModelTest(TestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
        # Create test service
        self.service = Service.objects.create(
            name="Haircut",
            description="Basic haircut service",
            duration=30,
            price=25.00
        )
        
        # Create test stylist
        self.stylist = Stylist.objects.create(
            name="John Doe",
            type="Senior",
            bio="Experienced hairstylist"
        )
        
        # Create test booking
        self.booking = Booking.objects.create(
            customer=self.user,
            stylist=self.stylist,
            service=self.service,
            message="Please style it modern",
            date=date(2024, 12, 20),
            time=time(14, 30),
            status=1
        )

    def test_booking_creation(self):
        self.assertTrue(isinstance(self.booking, Booking))
        expected_str = f"Booking for {self.user}, with {self.stylist} at 14:30:00 on 2024-12-20."
        self.assertEqual(str(self.booking), expected_str)

    def test_booking_fields(self):
        self.assertEqual(self.booking.customer, self.user)
        self.assertEqual(self.booking.stylist, self.stylist)
        self.assertEqual(self.booking.service, self.service)
        self.assertEqual(self.booking.message, "Please style it modern")
        self.assertEqual(self.booking.date, date(2024, 12, 20))
        self.assertEqual(self.booking.time, time(14, 30))
        self.assertEqual(self.booking.status, 1)

    def test_booking_status_choices(self):
        # Test all status choices
        self.booking.status = 0
        self.booking.full_clean()  # Should not raise validation error
        
        self.booking.status = 1
        self.booking.full_clean()  # Should not raise validation error
        
        self.booking.status = 2
        self.booking.full_clean()  # Should not raise validation error
        
        # Test invalid status
        self.booking.status = 3
        with self.assertRaises(ValidationError):
            self.booking.full_clean()

    def test_cascade_deletion(self):
        # Test if booking is deleted when user is deleted
        self.user.delete()
        with self.assertRaises(Booking.DoesNotExist):
            Booking.objects.get(pk=self.booking.pk)

        # Create new booking for testing stylist deletion
        new_user = User.objects.create_user(
            username='testuser2',
            password='testpass123'
        )
        new_booking = Booking.objects.create(
            customer=new_user,
            stylist=self.stylist,
            service=self.service,
            date=date(2024, 12, 21),
            time=time(15, 30),
            status=1
        )
        
        # Test if booking is deleted when stylist is deleted
        self.stylist.delete()
        with self.assertRaises(Booking.DoesNotExist):
            Booking.objects.get(pk=new_booking.pk)

    def test_ordering(self):
        # Create a new booking with a different date
        new_booking = Booking.objects.create(
            customer=self.user,
            stylist=self.stylist,
            service=self.service,
            date=date(2024, 12, 21),
            time=time(15, 30),
            status=1
        )
        
        # Get all bookings
        bookings = Booking.objects.all()
        
        # Check if the newest booking comes first
        self.assertEqual(bookings.first(), new_booking)
        self.assertEqual(bookings.last(), self.booking)