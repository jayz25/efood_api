from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('restaurents/<str:location>/', views.getRestaurentsByLocation),
    path('restaurents/addSome', views.addNewRestaurent),
    path('dishes/addSome', views.addDishes),
]