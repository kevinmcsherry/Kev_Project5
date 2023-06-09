# Generated by Django 3.2.19 on 2023-06-30 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kev_estore', '0005_rename_item_deliveryitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('accessories', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='kev_estore.accessories')),
                ('clothing', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='kev_estore.clothing')),
                ('clubs', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='kev_estore.clubs')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='kev_estore.order')),
            ],
        ),
        migrations.DeleteModel(
            name='DeliveryItem',
        ),
    ]
