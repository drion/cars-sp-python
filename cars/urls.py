from django.urls import path

from .views import CarList, CategoriesList, CarMakeList, CarModelList

urlpatterns = [
    path('', CarList.as_view(), name='car-list'),
    path('categories/', CategoriesList.as_view(), name='category-list'),
    path('makes/', CarMakeList.as_view(), name='make-list'),
    path('models/', CarModelList.as_view(), name='model-list'),
]