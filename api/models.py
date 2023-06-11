from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
import uuid

class Cuisine(models.Model):
    cuisine = models.CharField(primary_key=True, max_length=150)

    def __str__(self):
        return self.cuisine

class Restaurent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    cuisines = models.ManyToManyField(Cuisine, blank=False)
    logo = models.ImageField(upload_to="api/restaurent/images/", default="")
    ratings = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    delivery_time = models.IntegerField()
    live_discounts = models.CharField(max_length=150)
    average_price = models.IntegerField()

    def __str__(self):
        return self.name
