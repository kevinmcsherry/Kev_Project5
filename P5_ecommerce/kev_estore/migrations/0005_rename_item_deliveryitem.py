# Generated by Django 3.2.19 on 2023-06-30 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kev_estore', '0004_auto_20230630_1053'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Item',
            new_name='DeliveryItem',
        ),
    ]
