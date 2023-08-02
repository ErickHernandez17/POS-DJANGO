from django.urls import reverse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView 
from .forms import CountriesForm, CitiesForm, AddressForm
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