# Generated by Django 4.0 on 2022-09-18 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_product_temp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='temp',
        ),
    ]
