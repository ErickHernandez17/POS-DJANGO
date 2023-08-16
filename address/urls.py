from django.urls import path
from .views import CountriesCreatedView, CitiessCreatedView, AddressCreateView
from .views import CountriesListView,CountriesUpdateView,get_countries,update_country_ajax, delete_country
from .views import CitiesListView,CitiesUpdateView, get_cities,update_city_ajax,delete_city

urlpatterns = [
    path('country/create/', CountriesCreatedView.as_view(), name = 'create_country'),
    path('cities/create/', CitiessCreatedView.as_view(), name="create_city"),
    path('address/create', AddressCreateView.as_view(), name='create_address'),
    path('countries/', CountriesListView.as_view(), name='list_countries'),
    path('countries/update/<int:pk>/', CountriesUpdateView.as_view(), name="update-countries"),
    path('countries/update-ajax/<int:pk>/', update_country_ajax, name="update-country-ajax"),
    path('countries/delete/<int:country_id>/', delete_country, name="delete-country"),
    path('countries/get/', get_countries, name="get-countries"),
    path('cities/',CitiesListView.as_view(), name="list_cities"),
    path('cities/update/<int:pk>/', CitiesUpdateView.as_view(), name="update-cities"),
    path('cities/update-ajax/<int:pk>/', update_city_ajax, name="update-city-ajax"),
    path('cities/delete/<int:city_id>/', delete_city, name="delete-city"),
    path('cities/get/', get_cities, name="get-cities")
]