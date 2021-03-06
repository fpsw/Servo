# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 18:13
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servo', '0052_auto_20160321_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='flagged_by',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=[], size=None),
        ),
        migrations.AlterField(
            model_name='article',
            name='read_by',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=[], size=None),
        ),
    ]
