from django.urls import path
from .views import ProductsCreateView
urlpatterns = [
    path('create/', ProductsCreateView.as_view(), name='create_product')
]