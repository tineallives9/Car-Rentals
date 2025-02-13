from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


# Vehicle Model
class Vehicle(models.Model):
    vehicle_type = models.CharField(max_length=100)
    price_range = models.DecimalField(max_digits=10, decimal_places=2)
    fuel_type = models.CharField(max_length=50)
    transmission_type = models.CharField(max_length=50)
    

    def __str__(self):
        return f"{self.vehicle_type}"
    
    
# Booking Model
class Booking(models.Model):
    PAYMENT = [
        ("Successful", "Successful"),
        ("Failed", "Failed"),
    ]
        
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="bookings")
    location = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    availability = models.BooleanField(default=True)
    rent_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=50, null=True, blank=True, choices=PAYMENT)
    

    def __str__(self):
        return f"Booking by {self.user.get_full_name()} for {self.vehicle.vehicle_type} in {self.location} on {self.date}"
    


# Admin Model
class Admin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="admin_controls")
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="admin_vehicles")
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name="admin_bookings")
    manage_vehicles = models.BooleanField(default=False)
    manage_booking = models.BooleanField(default=False)
    manage_stats = models.BooleanField(default=False)
    track_revenue = models.BooleanField(default=False)
    track_popular_vehicles = models.BooleanField(default=False)
    track_customer_behavior = models.BooleanField(default=False)

    def __str__(self):
        return f"Admin - {self.user.username}"

# Notification Model
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    booking_confirmation = models.BooleanField(default=False)
    reminders = models.TextField(blank=True, null=True)
    promotions = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Notification for {self.user.nausernameme}"

# Loyalty Model
class Loyalty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="loyalty")
    discounts = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    free_rentals = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Loyalty for {self.user.username}"

# Reviews Model
class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    rate = models.PositiveIntegerField(default=0) 
    reviews = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Review by {self.user.username}"
