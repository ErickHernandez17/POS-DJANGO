from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView
from .models import Inventories
from .forms import InvetoriesForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class InventoriesCreateView(CreateView):
    template_name = 'products/product_create_form.html'
    form_class = InvetoriesForm
    success_url = reverse_lazy('create_inventory')
    
    def form_valid(self, form):
        
        form.instance.created_by = self.request.user
        form.instance.update_date = None
        form.instance.update_by = None
        
        response = super().form_valid(form)
        messages.success(self.request, 'Inventario creado exitosamente.')
        return redirect(self.success_url)
    
    
class InventoriesListView(ListView):
    model = Inventories
    template_name = 'inventories/inventory_list_view.html'  # Cambia esto al nombre de tu plantilla
    context_object_name = 'inventories'  # Nombre con el que se accederá a los objetos en la plantilla
    ordering = ['product']  # Ordenamiento de los objetos
    using = 'slave'
    def get_queryset(self):
        query = self.request.GET.get('q')  # Obtiene el valor de la barra de búsqueda
        if query:
            return Inventories.objects.using('slave').filter(inventory__icontains=query, state=True)
        return Inventories.objects.using('slave').filter(state=True).all()
    
    
class InventoryUpdateView(UpdateView):
    model = Inventories  # Modelo sobre el que se basa la vista
    form_class = InvetoriesForm
    template_name = 'inventories/update_inventory.html'
    context_object_name = 'inventory' 
    success_url = reverse_lazy('list_inventory')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            inventories = list(Inventories.objects.using('slave').select_related('product').filter(state=True).values('id','product__product', 'product__price', 'quantity','create_date'))
            if len(inventories) > 0:
                data = {"message": "success", 'inventories': inventories}
            else:
                data = {'message': 'Not Found'}
            return JsonResponse(data)
        
        return response
    
    
    
def get_inventories(_request):
    inventories = list(Inventories.objects.using('slave').select_related('product').filter(state=True).values('id','product__product', 'product__price', 'quantity','create_date'))
    if(len(inventories)>0):
        data = {"message":"Success",'inventories':inventories}
    else:
        data = {'message':'Not Found'}
    return JsonResponse(data)


@require_POST
def update_inventory_ajax(request, pk):
    category = get_object_or_404(Inventories, pk=pk)
    form = InvetoriesForm(request.POST, instance=category)
    inventories = list(Inventories.objects.using('slave').select_related('product').filter(status=True).values('id','product__product', 'product__price', 'quantity','create_date'))
    if form.is_valid():
        form.save()
        data = {"message":"Success",'inventories':inventories}
        return JsonResponse(data)
    else:
        return JsonResponse({'message': 'error'})
    

@csrf_exempt
def delete_inventory(request, inventory_id):
    try:
        category = Inventories.objects.using('slave').get(pk=inventory_id)
        category.state = False
        category.save()
        data = {"message": "success"}
    except Inventories.DoesNotExist:
        data = {"message": "error"}
    
    return JsonResponse(data)


