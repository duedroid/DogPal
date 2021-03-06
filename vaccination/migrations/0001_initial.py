# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 18:10
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dog', '0001_initial'),
        ('veterinarian', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VaccineFor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('routine', models.CharField(max_length=255)),
                ('note', models.TextField(blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('timeupdate', models.DateTimeField(auto_now=True)),
                ('appointment', models.ManyToManyField(related_name='vaccine_for', to='veterinarian.Appointment')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='VaccineRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('next_vaccine', models.DateField()),
                ('date_record', models.DateField(default=datetime.date.today)),
                ('note', models.TextField(blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('timeupdate', models.DateTimeField(auto_now=True)),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dog.Dog')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='VaccineStockDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='vaccine/%Y/%m/')),
                ('brand', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('serial', models.CharField(max_length=100)),
                ('mfg', models.DateField(default=datetime.date.today)),
                ('exp', models.DateField(default=datetime.date.today)),
                ('timestamp', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('timeupdate', models.DateTimeField(auto_now=True)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veterinarian.Hospital')),
                ('vaccinefor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vaccine_stock_detail', to='vaccination.VaccineFor')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.AddField(
            model_name='vaccinerecord',
            name='vaccine_stock',
            field=models.ManyToManyField(related_name='vaccine_record', to='vaccination.VaccineStockDetail'),
        ),
        migrations.AddField(
            model_name='vaccinerecord',
            name='veterinarian',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
