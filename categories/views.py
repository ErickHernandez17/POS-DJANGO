from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView, UpdateView, DetailView
from .forms import CategoryCreateForm
from .models import Categories
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class CategoryCreateView(CreateView):
    template_name = 'categories/category_create_form.html'
    form_class = CategoryCreateForm
    success_url = reverse_lazy('create_category')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Categoria creada exitosamente.')  # Agrega el mensaje de éxito
        return redirect(self.success_url)
    
    

class CategoriesListView(DetailView):
    model = Categories
    template_name = 'categories/category_list_view.html'
    context_object_name = 'categories'
    ordering = ['category']
    using = 'slave'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Categories.objects.using('slave').filter(category__icontains=query)
        return Categories.objects.using('slave').all()
    
    def get_object(self, queryset=None):
        return Categories.objects.using('slave').all()


class CategoryUpdateView(UpdateView):
    model = Categories  # Modelo sobre el que se basa la vista
    form_class = CategoryCreateForm
    template_name = 'categories/update_category.html'
    context_object_name = 'category' 
    success_url = reverse_lazy('list_category')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            categories = list(Categories.objects.values().filter(state=True))
            if len(categories) > 0:
                data = {"message": "success", 'categories': categories}
            else:
                data = {'message': 'Not Found'}
            return JsonResponse(data)
        
        return response
    
    
    
def get_categories(_request):
    categories = list(Categories.objects.using('slave').values().filter(state=True))
    
    if(len(categories)>0):
        data = {"message":"Success",'categories':categories}
    else:
        data = {'message':'Not Found'}
    return JsonResponse(data)

@require_POST
def update_category_ajax(request, pk):
    category = get_object_or_404(Categories, pk=pk)
    form = CategoryCreateForm(request.POST, instance=category)
    categories = list(Categories.objects.values().filter(state=True))
    if form.is_valid():
        form.save()
        data = {"message":"Success",'categories':categories}
        return JsonResponse(data)
    else:
        return JsonResponse({'message': 'error'})

@csrf_exempt
def delete_category(request, category_id):
    try:
        category = Categories.objects.get(pk=category_id)
        category.state = False
        category.save()
        data = {"message": "success"}
    except Categories.DoesNotExist:
        data = {"message": "error"}
    
    return JsonResponse(data)
