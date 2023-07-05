from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Restaurent, Menu, Dish, Cuisine
from .serializers import RestaurentSerializer, DishesSerializer, MenuSerializer, CuisineSerializer
from rest_framework import status

@api_view(['GET'])
def getData(requesst):
    data = [
    { "name": "Sunsetta" },
    { "name": "Apple" },
    { "name": "Berry" },
    { "name": "Watermelon" },
    { "name": "Pizaa" },
    { "name": "Jade Parcels" },
    { "name": "Sango Pearl" },
    { "name": "Razor" },
    ]
    return Response(data)

@api_view(['GET'])
def getRestaurentsByLocation(request, location):
    restaurents = Restaurent.objects.filter(location = location)
    serialized_restaurents = RestaurentSerializer(restaurents, many= True)
    return Response(serialized_restaurents.data)

@api_view(['POST'])
def addNewRestaurent(request):
    restaurents = RestaurentSerializer(data=request.data, many=True)
    if restaurents.is_valid():
        restaurents.save()
        return Response(restaurents.data, status=status.HTTP_201_CREATED)
    return Response(restaurents.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def addDishes(request):
    dishes = DishesSerializer(data=request.data, many=True)
    if dishes.is_valid():
        dishes.save()
        return Response(dishes.data, status=status.HTTP_201_CREATED)
    return Response(dishes.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getRestaurentById(request, id):
    restaurent = Restaurent.objects.filter(id=id)
    # Find out why do we get querySet name error when we try to use many=False here
    serialized_restaurent = RestaurentSerializer(restaurent, many=True)
    return Response(serialized_restaurent.data)

@api_view(['GET'])
def getMenuById(request, id):
    menu = Menu.objects.filter(id=id)
    serialized_menu = MenuSerializer(menu, many=True)
    return Response(serialized_menu.data)

@api_view(['GET'])
def getDishById(request, id):
    dish = Dish.objects.filter(id=id)
    serialized_dish = DishesSerializer(dish, many=True)
    return Response(serialized_dish.data)

@api_view(['GET'])
def getCuisines(request):
    cuisines = Cuisine.objects.filter(is_displaying=True)
    serialized_cuisines = CuisineSerializer(cuisines, many=True)
    return Response(serialized_cuisines.data)