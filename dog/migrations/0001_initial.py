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
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('blood_type', models.CharField(max_length=20)),
                ('breed', models.CharField(max_length=100)),
                ('current_weight', models.PositiveSmallIntegerField()),
                ('age', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('birth_day', models.DateField(default=datetime.date.today)),
                ('is_sterize', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('gender', models.PositiveSmallIntegerField(choices=[(1, 'Male'), (2, 'Female')])),
                ('micro_no', models.CharField(blank=True, max_length=100, null=True)),
                ('color_primary', models.CharField(blank=True, max_length=20, null=True)),
                ('color_secondary', models.CharField(blank=True, max_length=20, null=True)),
                ('location', models.TextField(max_length=300)),
                ('dominance', models.CharField(max_length=200)),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Alive'), (2, 'Death')], default=1)),
                ('timestamp', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('timeupdate', models.DateTimeField(auto_now=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='dog_image/%Y/%m/')),
                ('vector', models.CharField(blank=True, max_length=100, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('timeupdate', models.DateTimeField(auto_now=True)),
                ('dog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='picture', to='dog.Dog')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
