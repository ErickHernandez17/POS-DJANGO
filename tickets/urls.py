from django.urls import path
from .views import create_ticket, create_ticket_id
urlpatterns = [
    path('create/', create_ticket, name='create-ticket'),
    path('get-ticket-id/', create_ticket_id, name='get-ticket-id'),
]
