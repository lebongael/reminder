# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-15 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='order',
            field=models.IntegerField(),
        ),
    ]
