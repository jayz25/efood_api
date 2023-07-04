from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
import uuid

class Cuisine(models.Model):
    cuisine = models.CharField(primary_key=True, max_length=150)

    def __str__(self):
        return self.cuisine


class Dish(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    ratings = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    servings = models.CharField(max_length=150)
    image_url = models.URLField(default="", null=True, blank=True)

    def __str__(self):
        return self.name

class Menu(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150, default="")
    dishes = models.ManyToManyField(Dish, blank=False)
    cuisines = models.ManyToManyField(Cuisine, blank=False)

    def __str__(self):
        return self.name
    
class Restaurent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    cuisines = models.ManyToManyField(Cuisine, blank=False)
    logo = models.ImageField(upload_to="api/restaurent/images/", default="")
    image_url = models.URLField(default="", null=True, blank=True)
    ratings = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    delivery_time = models.IntegerField()
    live_discounts = models.CharField(max_length=150)
    average_price = models.IntegerField()
    menu_id = models.ForeignKey(Menu, on_delete=models.PROTECT, null=True)
    restaurent_page_image = models.URLField(default="", null=True, blank=True)


    def __str__(self):
        return self.name
