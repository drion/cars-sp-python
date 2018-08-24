from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .models import (
    Category,
    Car,
    CarMake,
    CarModel
)
from .serializers import CarSerializer, CategorySerializer, CarMakeSerializer, CarModelSerializer


class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def create(self, request, *args, **kwargs):
        make = CarMake.objects.get(uuid=request.data['make'])
        model = CarModel.objects.get(uuid=request.data['model'])

        data = request.data.copy()
        data["make"] = make
        data["model"] = model

        instance = Car.objects.create(**data)
        serializer = CarSerializer(instance)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class CategoriesList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CarMakeList(generics.ListAPIView):
    queryset = CarMake.objects.all()
    serializer_class = CarMakeSerializer


class CarModelList(generics.ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
