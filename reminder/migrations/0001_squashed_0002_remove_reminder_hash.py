# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-13 13:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('reminder', '0001_initial'), ('reminder', '0002_remove_reminder_hash')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_email', models.EmailField(max_length=254)),
                ('recipient_email', models.EmailField(max_length=254, verbose_name="recipient's email")),
                ('subject', models.CharField(max_length=78, verbose_name='reminder subject')),
                ('body', models.TextField(blank=True, max_length=2674, null=True, verbose_name='reminder text')),
                ('day_to_send', models.DateField()),
                ('time_to_send', models.TimeField()),
                ('is_sent', models.BooleanField(default=False)),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]