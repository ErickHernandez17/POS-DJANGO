from django.shortcuts import render, redirect
from .models import Ticket, Items
from products.models import Products
from .forms import TicketForm, ItemForm
from django.views.generic import View
from django.http import JsonResponse
from products.models import Products
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.contrib import messages
import json

""" def create_ticket(request):
    if request.method == 'POST':
        items_data = json.loads(request.body).get('items')
        if items_data:
            
            for item_data in items_data:
                print(item_data['product'])
                try:
                    ticket = Ticket.objects.get(pk=item_data['ticket_id'])
                    product = Products.objects.get(pk=item_data['product'])
                    item = Items(price=item_data['price'], quantity=item_data['quantity'])
                    item.ticket = ticket
                    item.product = product
                    item.save()
                    print('Item agregado exitosamente')
                except Exception as e:
                    messages.error(request, 'error al agregar los productos al ticket')
                    return redirect(reverse('create-ticket'))
     
            messages.success(request, 'Producto creado exitosamente.')
            return HttpResponse(reverse('create-ticket'))
        else:
            return JsonResponse({'error': 'No se proporcionaron elementos'}, status=400)
    else:
        products_available = Products.objects.filter(state=True)
        form = ItemForm(initial={'product': products_available})
    return render(request, 'tickets/create_ticket.html', {'form': form}) """

class CreateTicketView(View):
    template_name = 'tickets/create_ticket.html'
    item_form_class = ItemForm
    success_url = reverse_lazy('create-ticket')
    
    def get(self, request, *args, **kwargs):
        products_available = Products.objects.filter(state=True)
        form = self.item_form_class(initial={'product':products_available})
        return render(request, self.template_name, {'form': form, 'messages': messages.get_messages(request)})


    def post(self, request, *args, **kwargs):
        items_data = json.loads(request.body).get('items')
        if items_data:
            for item_data in items_data:
                try:
                    ticket = Ticket.objects.get(pk=item_data['ticket_id'])
                    product = Products.objects.get(pk=item_data['product'])
                    item = Items(price=item_data['price'],quantity=item_data['quantity'])
                    item.ticket = ticket
                    item.product = product
                    item.save()
                except Exception as e:
                    messages.error(request, 'Error al agregar los productos/n'+str(e))
                    return JsonResponse({'error':str(e)}, status = 400)
            messages.success(request, 'Productos agregados exitosamente')
            return redirect(self.success_url)
        else:
            return JsonResponse({'error': 'No se proporcionaron elementos'}, status=400)
        
        
        

def create_ticket_id(request):
    if request.method == 'POST':
        user_id = json.loads(request.body).get('user_id')
        if user_id:
            ticket = Ticket.objects.create(create_by_id=user_id, update_by_id=user_id)
            return JsonResponse({'ticket_id':ticket.id})
        else:
            return JsonResponse({'error':'ID de usuario no encontrado'},status=400)
    return JsonResponse({'error': 'Método no permitido'}, status=405)
