from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CategoryCreateForm
# Create your views here.

class CategoryCreateView(CreateView):
    template_name = 'categories/category_create_form.html'
    form_class = CategoryCreateForm
    success_url = reverse_lazy('create_category')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Categoria creada exitosamente.')  # Agrega el mensaje de éxito
        return redirect(self.success_url)
