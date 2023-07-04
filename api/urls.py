from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('restaurents/<str:location>/', views.getRestaurentsByLocation),
    path('restaurents/addSome', views.addNewRestaurent),
    path('dishes/addSome', views.addDishes),
    path('dishes/getSingle/<str:id>/', views.getDishById),
    path('restaurents/getSingle/<str:id>/', views.getRestaurentById),
    path('menu/<str:id>/', views.getMenuById),
]