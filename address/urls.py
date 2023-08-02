from django.urls import path
from .views import CountriesCreatedView, CitiessCreatedView, AddressCreateView

urlpatterns = [
    path('country/create/', CountriesCreatedView.as_view(), name = 'create_country'),
    path('cities/create/', CitiessCreatedView.as_view(), name="create_city"),
    path('address/create', AddressCreateView.as_view(), name='create_address')
]