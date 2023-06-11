from rest_framework import serializers
from . import models

class RestaurentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Restaurent
        fields = '__all__'