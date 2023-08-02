from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView
from .forms import ProductsCreateForm
from django.urls import reverse_lazy
from django.contrib import messages
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