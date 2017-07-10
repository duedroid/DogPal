# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-10 14:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doginformation', '0001_initial'),
        ('veterinarian', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VaccinationFor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('routine', models.CharField(max_length=100)),
                ('note', models.TextField(blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('timeupdate', models.DateTimeField(auto_now=True)),
                ('appointment', models.ManyToManyField(to='veterinarian.Appointment')),
                ('vethos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veterinarian.VetHos')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='VaccinationRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('next_vaccine', models.DateField()),
                ('date_record', models.DateField(default=datetime.date.today)),
                ('note', models.TextField(blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('timeupdate', models.DateTimeField(auto_now=True)),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dogvaccine', to='doginformation.Dog')),
                ('vaccine_for', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vaccinationrecord', to='vaccination.VaccinationFor')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
