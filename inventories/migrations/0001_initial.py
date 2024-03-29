# Generated by Django 4.2.3 on 2023-08-02 01:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0005_alter_products_create_by_alter_products_update_by'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Cantidad')),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('create_dete', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('update_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de modificacion')),
                ('create_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='create_by_inventory', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='products.products', verbose_name='Producto')),
                ('update_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='update_by_inventory', to=settings.AUTH_USER_MODEL, verbose_name='Modificado por')),
            ],
            options={
                'verbose_name': 'Inventario',
                'verbose_name_plural': 'Inventarios',
                'ordering': ['product', '-create_dete', '-update_date'],
            },
        ),
    ]
