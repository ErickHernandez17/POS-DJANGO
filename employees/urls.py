from django.urls import path
from .views import EmployeeCreateView, UserCreateView

urlpatterns = [
    path('employee/create/', EmployeeCreateView.as_view(), name = 'create_employee'),
    path('user/create/', UserCreateView.as_view(), name="create_user"),
]