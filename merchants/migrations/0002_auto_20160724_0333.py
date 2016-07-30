# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-24 03:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchant',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='merchant',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]