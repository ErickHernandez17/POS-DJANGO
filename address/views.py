from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from .forms import CountriesForm, CitiesForm, AddressForm
from .models import Cities, Countries
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.contrib import messages

class CountriesCreatedView(CreateView):
    template_name = 'address/country_created_form.html'
    form_class = CountriesForm
    success_url = reverse_lazy('create_country')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'País agregado exitosamente.')  # Agrega el mensaje de éxito
        return redirect(self.success_url)
    
class CitiessCreatedView(CreateView):
    template_name = 'address/city_created_form.html'
    form_class = CitiesForm
    success_url = reverse_lazy('create_city')
    
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Ciudad agregadada exitosamente.')  # Agrega el mensaje de éxito
        return redirect(self.success_url)
    
class AddressCreateView(CreateView):
    template_name = 'address/address_create_form.html'
    form_class = AddressForm
    success_url = reverse_lazy('create_employee')
    
    def get_initial(self):
        initial = super().get_initial()
        self.user_id = self.request.GET.get('user_id')
        if self.user_id:
            initial['user'] = self.user_id
        return initial
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Direccion guardada exitosamente.')  # Agrega el mensaje de éxito

        # Obtiene el ID de la dirección recién creada.
        address_id = self.object.id

        # Redirige a la vista EmployeeCreateView y pasa el ID de la dirección en la URL.
        return redirect(reverse('create_employee') + f'?address_id={address_id}&user_id={self.request.GET.get("user_id")}')
    
    
class CountriesListView(ListView):
    model = Countries
    template_name = 'address/list.html'
    context_object_name = 'items'
    ordering = ['country']
    using = 'slave'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'PAISES'
        return context 
    
class CountriesUpdateView(UpdateView):
    model = Countries
    form_class = CountriesForm
    template_name = 'address/update.html'
    context_object_name = 'item'
    success_url = reverse_lazy('list_countries')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            countries = list(Countries.objects.using('slave').values())
            if len(countries) >= 0:
                data = {"message": "success", 'items': countries}
                
def get_countries(request):
    items = list(Countries.objects.using('slave').values())
    if(len(items)>-1):
        data = {'message':'Success', 'items':items}
    else:
        data = {'data':'Not Found'}
    return JsonResponse(data)

@require_POST
def update_country_ajax(request, pk):
    product = get_object_or_404(CountriesForm, pk=pk)
    form = CountriesForm(request.POST, instance=product)
    items = list(Countries.objects.using('slave').values())
    if form.is_valid():
        form.save()
        data = {"message":"Success",'items':items}
        return JsonResponse(data)
    else:
        return JsonResponse({'message': 'error'})
    
    
@csrf_exempt
def delete_country(request, country_id):
    try:
        country = Countries.objects.using('slave').get(pk=country_id)
        country.state = False
        country.save()
        data = {"message": "success"}
    except Countries.DoesNotExist:
        data = {"message": "error"}
    
    return JsonResponse(data)



class CitiesListView(ListView):
    model = Cities
    template_name = 'address/list.html'
    context_object_name = 'items'
    ordering = ['city']
    using = 'slave'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'CIUDADES'
        return context 
    
class CitiesUpdateView(UpdateView):
    model = Cities
    form_class = CitiesForm
    template_name = 'address/update.html'
    context_object_name = 'item'
    success_url = reverse_lazy('list_cities')
    using = 'default'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            cities = list(Cities.objects.values())
            if len(cities) >= 0:
                data = {"message": "success", 'items': cities}
                
def get_cities(request):
    items = list(Cities.objects.using('slave').values())
    if(len(items)>-1):
        data = {'message':'Success', 'items':items}
    else:
        data = {'data':'Not Found'}
    return JsonResponse(data)

@require_POST
def update_city_ajax(request, pk):
    cities = get_object_or_404(CitiesForm, pk=pk)
    form = CountriesForm(request.POST, instance=cities)
    items = list(Cities.objects.using('slave').values())
    if form.is_valid():
        form.save()
        data = {"message":"Success",'items':items}
        return JsonResponse(data)
    else:
        return JsonResponse({'message': 'error'})
    
    
@csrf_exempt
def delete_city(request, city_id):
    try:
        city = Cities.objects.using('slave').get(pk=city_id)
        city.state = False
        city.save()
        data = {"message": "success"}
    except Countries.DoesNotExist:
        data = {"message": "error"}
    
    return JsonResponse(data)