# Generated by Django 3.2.12 on 2022-03-23 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0019_ordersupplier_vendors'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordersupplier',
            old_name='vendors',
            new_name='vendor',
        ),
    ]