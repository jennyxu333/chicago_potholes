# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-13 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('potholes_site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='zipcode',
            field=models.IntegerField(default=60637),
        ),
    ]
