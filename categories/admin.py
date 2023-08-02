from django.contrib import admin
from .models import Categories
# Register your models here.

class CategoriesAdmin(admin.ModelAdmin):
    readonly_fields = ('create_date','update_date')
    
admin.site.register(Categories, CategoriesAdmin)
