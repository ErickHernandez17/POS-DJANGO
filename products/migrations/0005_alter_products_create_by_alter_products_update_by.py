# Generated by Django 4.2.3 on 2023-08-02 01:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0004_alter_products_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='create_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='create_by_product', to=settings.AUTH_USER_MODEL, verbose_name='Creado por'),
        ),
        migrations.AlterField(
            model_name='products',
            name='update_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='update_by_product', to=settings.AUTH_USER_MODEL, verbose_name='Modificado por'),
        ),
    ]