# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-30 15:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_usermodel'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='usermodel',
            table='axf_usermodel',
        ),
    ]
