# Generated by Django 5.1.4 on 2025-01-23 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_created_at_product_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='product',
            name='users',
        ),
    ]
