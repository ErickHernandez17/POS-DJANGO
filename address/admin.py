from django.contrib import admin
from .models import Countries, Cities, Address
# Register your models here.

admin.site.register(Countries)
admin.site.register(Cities)
admin.site.register(Address)
