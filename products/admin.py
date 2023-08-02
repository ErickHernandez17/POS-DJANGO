from django.contrib import admin
from .models import Products
# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    readonly_fields = ('create_date', 'update_date','create_by','update_by')
    
admin.site.register(Products, ProductsAdmin)
