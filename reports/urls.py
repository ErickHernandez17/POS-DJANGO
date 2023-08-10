from django.urls import path
from .views import get_chart,reports_index
urlpatterns = [
    path('', reports_index, name='reports'),
    path('get_chart/', get_chart, name='get_chart')
]
