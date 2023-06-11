from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('restaurents/<str:location>/', views.getRestaurentsByLocation)
]