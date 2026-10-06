"""Dealership data models: car makes/models, dealers and reviews."""

from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class CarMake(models.Model):
    """A car manufacturer, e.g. Toyota."""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, default='')

    def __str__(self):
        return f"CarMake: {self.name}"


class CarModel(models.Model):
    """A car model belonging to a make, e.g. Camry."""
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    COUPE = 'Coupe'
    BODY_CHOICES = [(SEDAN, 'Sedan'), (SUV, 'SUV'), (WAGON, 'Wagon'), (COUPE, 'Coupe')]
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body_type = models.CharField(max_length=20, choices=BODY_CHOICES, default=SEDAN)
    year = models.IntegerField(default=2024)

    def __str__(self):
        return f"CarModel: {self.make.name} {self.name} ({self.year})"


class Dealer(models.Model):
    """A dealership branch."""
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100, default='')
    state = models.CharField(max_length=2, default='')
    address = models.CharField(max_length=200, default='')
    zip_code = models.CharField(max_length=10, default='')
    phone = models.CharField(max_length=20, default='')

    def __str__(self):
        return f"Dealer: {self.name} ({self.city}, {self.state})"


class Review(models.Model):
    """A customer review for a dealer, with sentiment label."""
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    rating = models.IntegerField(default=5)
    sentiment = models.CharField(max_length=20, default='neutral')
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"Review by {self.user.username} for {self.dealer.name}: {self.sentiment}"
