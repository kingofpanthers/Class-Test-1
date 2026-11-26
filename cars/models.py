from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models


class Car(models.Model):
    class Fuel(models.TextChoices):
        PETROL = "Petrol"
        DIESEL = "Diesel"
        HYBRID = "Hybrid"
        ELECTRIC = "Electric"
        OTHER = "Other"

    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    year = models.IntegerField(validators=[MinValueValidator(1886)])
    price = models.DecimalField(
        max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal("0"))]
    )
    description = models.TextField()
    is_available = models.BooleanField(default=True)

    fuel_type = models.CharField(max_length=20, choices=Fuel.choices, default=Fuel.PETROL)

    def __str__(self):
        return self.name
