from django.urls import path
from .views import EmployeeCreateView, UserCreateView
from .views import EmployeesListView, get_employees, update_employee_ajax, delete_employee

urlpatterns = [
    path('employee/create/', EmployeeCreateView.as_view(), name = 'create_employee'),
    path('user/create/', UserCreateView.as_view(), name="create_user"),
    path('', EmployeesListView.as_view(), name='list_employees'),
    path('get/', get_employees, name="get-employees")
]