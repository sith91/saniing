# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-11-20 14:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20181120_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='"profile"+', to=settings.AUTH_USER_MODEL),
        ),
    ]