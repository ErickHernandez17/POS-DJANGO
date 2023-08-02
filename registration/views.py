from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.urls import reverse_lazy
# Create your views here.
# def logout_view(request):
#     logout(request)
#     return redirect((reverse_lazy('login')))