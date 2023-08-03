from django.db import models
from products.models import Products
from django.contrib.auth.models import User
# Create your models here.
class Inventories(models.Model):
    product = models.OneToOneField(Products, on_delete=models.RESTRICT, verbose_name='Producto')
    quantity = models.PositiveIntegerField(verbose_name='Cantidad')
    state = models.BooleanField(default=True, verbose_name='Estado')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    create_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Creado por', related_name='create_by_inventory')
    update_date = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='Fecha de modificacion')
    update_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Modificado por', related_name='update_by_inventory')

    class Meta:
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'
        ordering = ['product','-create_date','-update_date']
        
    def __str__(self):
        return self.product