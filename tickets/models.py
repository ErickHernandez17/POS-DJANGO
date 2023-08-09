from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Ticket(models.Model):
    create_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Creado por', related_name='create_ticket_by')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    update_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Modificado por', related_name='update_ticket_by')
    update_date = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='Fecha de creacion')
    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
        ordering = ['-create_date']
    def __str__(self):
        return '{} {} {}'.format(self.id, self.create_by ,self.create_date)
    
class Items(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.SET_NULL, null=True, verbose_name='Ticket')
    product = models.ForeignKey('products.Products', on_delete=models.SET_NULL, null=True, verbose_name='Producto')
    price = models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Precio unitario')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Cantidad')
    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        ordering = ['-ticket','product']
    def __str__(self):
        return '{} {}'.format(self.id, self.ticket ,self.product)
    
    
    