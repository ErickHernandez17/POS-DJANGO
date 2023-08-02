from django.db import models
from django.contrib.auth.models import User
from address.models import Address
# Create your models here.
class Employee(models.Model):
    rfc = models.CharField(max_length=13, verbose_name='RFC')
    curp = models.CharField(max_length=18, verbose_name='CURP')
    first_name = models.CharField(max_length=250, verbose_name='Nombres')
    last_name = models.CharField(max_length=300, verbose_name='Apellidos')
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    address = models.OneToOneField(Address, on_delete=models.RESTRICT)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empeados'
        ordering = ['last_name','first_name','rfc']


    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.rfc}'