# Generated by Django 3.2.19 on 2023-06-23 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kev_estore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clothing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Clubs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Product',
            new_name='Accessories',
        ),
        migrations.RemoveField(
            model_name='item',
            name='product',
        ),
        migrations.AddField(
            model_name='item',
            name='clothing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='kev_estore.clothing'),
        ),
    ]
