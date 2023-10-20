from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name

class Table(models.Model):
    capacity = models.PositiveIntegerField()  # Assuming you want to use capacity
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return f"Table for {self.capacity}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    booking_date = models.DateTimeField()
    number_of_guests = models.PositiveIntegerField()

    def __str__(self):
        return f"Booking by {self.user} for {self.number_of_guests} guests"

class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

