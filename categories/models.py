from django.db import models

# Create your models here.
class Categories(models.Model):
    category = models.CharField(max_length=45)
    state = models.BooleanField(verbose_name='Estado', default=True)
    create_date = models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')
    update_date = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='Fecha de modificacion')
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['category']


    def __str__(self):
        return self.category