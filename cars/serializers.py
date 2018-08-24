from rest_framework import serializers
from .models import (
    Category,
    CarMake,
    CarModel,
    Car
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('uuid', 'name', 'start_year', 'end_year')


class CarMakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMake
        fields = ('uuid', 'name')


class CarModelSerializer(serializers.ModelSerializer):
    make = serializers.StringRelatedField(source='make.uuid')

    class Meta:
        model = CarModel
        fields = ('uuid', 'name', 'make')


class CarSerializer(serializers.ModelSerializer):
    make = serializers.UUIDField(source='make.uuid')
    model = serializers.UUIDField(source='model.uuid')
    category = serializers.StringRelatedField(source='category.uuid')

    class Meta:
        model = Car
        fields = ('uuid', 'make', 'model', 'category', 'price', 'year', 'owner')
        read_only_fields = ('uuid', 'category')
