from rest_framework import generics

from .models import (
    Category,
    Car
)
from .serializers import CarSerializer


class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def perform_create(self, serializer):
        category = Category.choose_category(int(serializer.validated_data.get('year')))
        serializer.save(category=category)
