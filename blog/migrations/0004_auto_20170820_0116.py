# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-19 19:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_guy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guy',
            name='name',
        ),
        migrations.DeleteModel(
            name='Guy',
        ),
    ]
