from django.urls import path
from .views import CreateTicketView, create_ticket_id
urlpatterns = [
    path('create/', CreateTicketView.as_view(), name='create-ticket'),
    path('get-ticket-id/', create_ticket_id, name='get-ticket-id'),
]
