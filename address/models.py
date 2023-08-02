from django.db import models

# Create your models here.
class Countries(models.Model):
    country = models.CharField(max_length=45, verbose_name='País')

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Países'
        ordering = ['country']

    

    def __str__(self):
        return self.country
    

class Cities(models.Model):
    city = models.CharField(max_length=45, verbose_name='Ciudad')
    country = models.ForeignKey(Countries, on_delete=models.RESTRICT, verbose_name='País')

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
        ordering = ['country']

    def __str__(self):
        return f'{self.country}, {self.city}'
    

class Address(models.Model):
    address = models.CharField(max_length=300, verbose_name='Direcccion')
    cp = models.CharField(max_length=5, verbose_name='Codigo postal')
    city = models.ForeignKey(Cities, on_delete=models.RESTRICT, verbose_name='Ciudad')

    class Meta:
        verbose_name = 'Direccion'
        verbose_name_plural = 'Direcciones'
        ordering = ['address']

    

    def __str__(self):
        return f'{self.address} {self.cp}. {self.city}'