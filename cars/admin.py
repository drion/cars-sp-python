from django.contrib import admin

from .models import (
    Category,
    Car
)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'model', 'make', 'category', 'price', 'year', 'owner')
    readonly_fields = ('category', )

    def make(self, car):
        return car.model.make


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'name', 'start_year', 'end_year')
