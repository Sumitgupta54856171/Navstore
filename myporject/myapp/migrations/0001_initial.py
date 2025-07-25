# Generated by Django 5.2.4 on 2025-07-14 17:13

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=30)),
                ('createat', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'myapp_user',
            },
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.CharField(max_length=250)),
                ('productname', models.CharField(max_length=250)),
                ('productprice', models.IntegerField()),
                ('productquantity', models.IntegerField()),
                ('image', models.ImageField(upload_to='products/')),
                ('productdescription', models.CharField(max_length=5000)),
                ('productbrand', models.CharField(max_length=250)),
                ('productcolor', models.CharField(max_length=250)),
                ('productmaterial', models.CharField(max_length=250)),
                ('category', models.CharField(max_length=250)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
            options={
                'db_table': 'myapp_customer',
            },
        ),
    ]
