from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Restaurent
from .serializers import RestaurentSerializer

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

