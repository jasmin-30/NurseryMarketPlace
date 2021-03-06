# Generated by Django 2.2.13 on 2020-06-09 16:09

import Nurseryshop.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Nurseryshop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nursery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('address', models.TextField(verbose_name='Address')),
                ('opening_time', models.TimeField(verbose_name='Opening Time')),
                ('closing_time', models.TimeField(verbose_name='Closing Time')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User ID')),
            ],
            options={
                'verbose_name': 'Nursery',
                'verbose_name_plural': 'Nurseries',
            },
        ),
        migrations.CreateModel(
            name='Plants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(upload_to=Nurseryshop.models.upload_img_to, verbose_name='Plant Image')),
                ('nursery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Nurseryshop.Nursery', verbose_name='Nursery')),
            ],
            options={
                'verbose_name': 'Plant',
                'verbose_name_plural': 'Plants',
            },
        ),
    ]
