from django.contrib import admin
from .models import Restaurent, Cuisine, Dish, Menu

admin.site.register(Restaurent)
admin.site.register(Cuisine)
admin.site.register(Dish)
admin.site.register(Menu)