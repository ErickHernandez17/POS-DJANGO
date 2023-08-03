from django.contrib import admin
from .models import Inventories
# Register your models here.

class InvetoriesAdmin(admin.ModelAdmin):
    readonly_fields = ('create_date', 'update_date','create_by','update_by')
    
admin.site.register(Inventories, InvetoriesAdmin)
