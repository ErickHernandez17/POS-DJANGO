from django.shortcuts import render, redirect
from .models import Ticket, Items
from .forms import TicketForm, ItemForm
from django.http import JsonResponse
from products.models import Products
import json

def create_ticket(request):
    if request.method == 'POST':
        items_data = json.loads(request.body).get('items')
        if items_data:
            ticket_id = items_data[0]['ticket_id']  # Tomar el ticket_id del primer elemento
            for item_data in items_data:
                form = ItemForm(item_data)
                if form.is_valid():
                    item = form.save(commit=False)
                    item.ticket_id = ticket_id  # Asignar el ticket_id al elemento
                    item.save()
            return JsonResponse({'ticket_id': ticket_id})
        else:
            return JsonResponse({'error': 'No se proporcionaron elementos'}, status=400)
    else:
        products_available = Products.objects.filter(state=True)
        form = ItemForm(initial={'product': products_available})
    return render(request, 'tickets/create_ticket.html', {'form': form})

def create_ticket_id(request):
    if request.method == 'POST':
        user_id = json.loads(request.body).get('user_id')
        if user_id:
            ticket = Ticket.objects.create(create_by_id=user_id, update_by_id=user_id)
            return JsonResponse({'ticket_id':ticket.id})
        else:
            return JsonResponse({'error':'ID de usuario no encontrado'},status=400)
    return JsonResponse({'error': 'Método no permitido'}, status=405)
