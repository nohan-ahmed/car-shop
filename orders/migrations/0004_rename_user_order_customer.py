# Generated by Django 5.0.3 on 2024-06-10 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='customer',
        ),
    ]