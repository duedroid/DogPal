# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 15:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doginformation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AntiParasitics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('next_dose', models.DateField()),
                ('date_record', models.DateField(default=datetime.date.today)),
                ('veterinarian', models.CharField(max_length=100)),
                ('note', models.TextField(blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('timeupdate', models.DateTimeField(auto_now=True)),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doginformation.Dog')),
            ],
        ),
        migrations.CreateModel(
            name='Therapy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('routine', models.CharField(max_length=200)),
                ('note', models.TextField(blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('timeupdate', models.DateTimeField(auto_now=True)),
                ('antiparasitics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='antiparasitics.AntiParasitics')),
            ],
        ),
    ]
