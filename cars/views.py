from rest_framework import generics

from .models import (
    Category,
    Car
)
from .serializers import CarSerializer


class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
