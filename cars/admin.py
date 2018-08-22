from django.contrib import admin

from .models import (
    Category,
    Car
)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'make', 'model', 'category', 'price', 'year', 'owner')
    readonly_fields = ('category', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'name', 'start_year', 'end_year')
