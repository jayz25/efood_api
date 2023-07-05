from rest_framework import serializers
from . import models

class RestaurentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Restaurent
        fields = '__all__'

class DishesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Dish
        fields = '__all__'
    
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Menu
        fields = '__all__'

class CuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cuisine
        fields = '__all__'