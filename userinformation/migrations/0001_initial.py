# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 15:09
from __future__ import unicode_literals

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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel_1', models.CharField(max_length=20)),
                ('tel_2', models.CharField(blank=True, max_length=20)),
                ('address', models.TextField(max_length=300)),
                ('lineid', models.CharField(max_length=50)),
                ('facebook', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('timeupdate', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
