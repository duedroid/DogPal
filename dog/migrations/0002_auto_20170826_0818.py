# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 08:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='location',
            field=models.TextField(),
        ),
    ]
