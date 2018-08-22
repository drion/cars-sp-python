from rest_framework import serializers
from .models import (
    Category,
    Car
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('uuid', 'name', 'start_year', 'end_year')


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('uuid', 'make', 'model', 'category', 'price', 'year')
