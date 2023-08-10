"""
URL configuration for POS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('category/', include('categories.urls')),
    path('product/', include('products.urls')),
    path('inventory/', include('inventories.urls')),
    path('reports/', include('reports.urls')),
    path('existens/', include('existens.urls')),
    path('address/',include('address.urls')),
    path('employee/', include('employees.urls')),
    path('tickets/', include('tickets.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
