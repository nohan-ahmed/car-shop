# Generated by Django 5.0.3 on 2024-06-10 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_order_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='qountity',
            new_name='quantity',
        ),
    ]
