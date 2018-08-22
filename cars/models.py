import sys
import uuid as uuid_lib

from django.db import models

# Constants for Categories
MIN_YEAR = 0
MAX_YEAR = 3000


class Car(models.Model):
    uuid = models.UUIDField(
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    category = models.OneToOneField(
        'Category',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    price = models.DecimalField(max_digits=35, decimal_places=10)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.make} {self.model}"


class Category(models.Model):
    uuid = models.UUIDField(
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False
    )
    start_year = models.PositiveIntegerField(default=MIN_YEAR)  # Set 0 if value is not set
    end_year = models.PositiveIntegerField(default=MAX_YEAR)  # Set max int if value not set
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    @staticmethod
    def choose_category(year):
        try:
            return Category.objects.get(start_year__lte=year, end_year__gt=year)
        except models.ObjectDoesNotExist:
            return None
