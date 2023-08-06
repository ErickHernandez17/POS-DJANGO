from django.urls import path
from .views import existens_list_view
urlpatterns = [
    path('', existens_list_view, name='existens')
]
