from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import EmployeeFormCreation, UserFormCreation
# Create your views here.
class UserCreateView(CreateView):
    template_name = 'employees/user_create_form.html'  # Reemplaza 'tu_template_de_creacion_de_usuario.html' por la ruta a tu template
    form_class = UserFormCreation
    success_url = reverse_lazy('create_address') 
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Usuario guardado exitosamente.')  # Agrega el mensaje de éxito
        user_id = self.object.id
        return redirect(reverse('create_address') + f'?user_id={user_id}')
    
    
class EmployeeCreateView(CreateView):
    template_name = 'employees/employee_create_form.html'  # Reemplaza 'tu_template_de_creacion_de_usuario.html' por la ruta a tu template
    form_class = EmployeeFormCreation
    success_url = reverse_lazy('home') 
    
    def form_valid(self, form):
        # Aquí, el formulario aún no ha sido guardado en la base de datos.
        # Así que, establecemos manualmente los campos user y address con los valores de la URL.
        form.instance.user_id = self.request.GET.get('user_id')
        form.instance.address_id = self.request.GET.get('address_id')
        
        # Ahora, llamamos al método form_valid de la clase base para guardar el objeto Employee en la base de datos.
        response = super().form_valid(form)
        messages.success(self.request, 'Empleado creado exitosamente.')  # Agrega el mensaje de éxito
        return response
    
    def get_initial(self):
        initial = super().get_initial()
        # Obtener el ID del usuario y la dirección de la URL si están disponibles
        user_id = self.request.GET.get('user_id')
        address_id = self.request.GET.get('address_id')
        print(user_id)
        print(address_id)
        if user_id:
            initial['user'] = user_id
        if address_id:
            initial['address'] = address_id
        return initial