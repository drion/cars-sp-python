from django.urls import path

from .views import CarList

urlpatterns = [
    path('', CarList.as_view(), name='car-list'),
]