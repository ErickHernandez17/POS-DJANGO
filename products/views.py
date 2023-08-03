from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, UpdateView
from .forms import ProductsCreateForm
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Products
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


class ProductsCreateView(CreateView):
    template_name = 'products/product_create_form.html'
    form_class = ProductsCreateForm
    success_url = reverse_lazy('create_product')
    
    def form_valid(self, form):
        
        form.instance.created_by = self.request.user
        form.instance.update_date = None
        form.instance.update_by = None
        
        response = super().form_valid(form)
        messages.success(self.request, 'Producto creado exitosamente.')
        return redirect(self.success_url)
    
    
class ProductsListView(ListView):
    model = Products
    template_name = 'products/products_list_view.html'  # Cambia esto al nombre de tu plantilla
    context_object_name = 'products'  # Nombre con el que se accederá a los objetos en la plantilla
    ordering = ['product']  # Ordenamiento de los objetos

    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset = Products.objects.all()
        if query:
            queryset = Products.objects.filter(product__icontains=query)
        return queryset
    

class ProductUpdateView(UpdateView):
    model = Products
    form_class = ProductsCreateForm
    template_name = 'products/update_product.html'
    success_url = reverse_lazy('list_product')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            products = list(Products.objects.values().filter(state=True))
            if len(products) > -1:
                data = {"message": "success", 'categories': products}
            else:
                data = {'message': 'Not Found'}
            return JsonResponse(data)
        
        return response


def get_products(_request):
    products = list(Products.objects.values().filter(state=True))
    if(len(products)>-1):
        data = {'message':'Success', 'products':products}
    else:
        data = {'data':'Not Found'}
    return JsonResponse(data)


@require_POST
def update_category_ajax(request, pk):
    product = get_object_or_404(Products, pk=pk)
    form = ProductsCreateForm(request.POST, instance=product)
    products = list(Products.objects.values().filter(state=True))
    if form.is_valid():
        form.save()
        data = {"message":"Success",'categories':products}
        return JsonResponse(data)
    else:
        return JsonResponse({'message': 'error'})
    
    
@csrf_exempt
def delete_product(request, product_id):
    try:
        category = Products.objects.get(pk=product_id)
        category.state = False
        category.save()
        data = {"message": "success"}
    except Products.DoesNotExist:
        data = {"message": "error"}
    
    return JsonResponse(data)