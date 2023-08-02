from django.db import models
from django.contrib.auth.models import User
from categories.models import Categories
# Create your models here.
class Products(models.Model):
    product = models.CharField(max_length=45, verbose_name='Producto')
    tradermark = models.CharField(max_length=45, verbose_name='Fabricante')
    presentation = models.CharField(max_length=45, verbose_name='Presentacion')
    price = models.DecimalField(decimal_places=2, max_digits=7, verbose_name='precio')
    description = models.TextField(verbose_name='Descripcion', null=True, blank=True)
    serial_number = models.CharField(max_length=45, verbose_name='Numero serial')
    category = models.ForeignKey(Categories, verbose_name='Categoria', on_delete=models.RESTRICT)
    state = models.BooleanField(default=True, verbose_name='EStado')
    create_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Creado por', related_name='create_by_product')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    update_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Modificado por', related_name='update_by_product')
    update_date = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='Fecha de modificacion')
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['product','-create_date','-update_date']
        
    
    def __str__(self):
        return f'{self.product} {self.presentation}'