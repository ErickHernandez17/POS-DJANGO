from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import redirect
from django.urls import reverse
from django.http import JsonResponse
from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import EmployeeFormCreation, UserFormCreation
from .models import Employee
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
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
    
class EmployeesListView(ListView):
    model = Employee
    template_name = 'employees/list_employee.html'
    context_object_name = 'employees'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Employee.objects.filter(state=True, usernme__icontains=query)
        else:
            return  Employee.objects.filter(state=True).all()
        
        
def get_employees(_request):
    employees = list(Employee.objects.values().all())
    if(len(employees)>-1):
        data = {'message':'Success', 'employees':employees}
    else:
        data = {'data':'Not Found'}
    return JsonResponse(data)


@require_POST
def update_employee_ajax(request, pk):
    product = get_object_or_404(Employee, pk=pk)
    form = EmployeeFormCreation(request.POST, instance=product)
    employees = list(Employee.objects.values().filter(state=True))
    if form.is_valid():
        form.save()
        data = {"message":"Success",'employees':employees}
        return JsonResponse(data)
    else:
        return JsonResponse({'message': 'error'})


@csrf_exempt
def delete_employee(request, product_id):
    try:
        employee = Employee.objects.get(pk=product_id)
        employee.delete()
        data = {"message": "success"}
    except Employee.DoesNotExist:
        data = {"message": "error"}
    
    return JsonResponse(data)

    