# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-27 10:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gprojects', '0027_gtask_predecessors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gtask',
            name='children',
            field=models.ManyToManyField(blank=True, to='gprojects.Gtask'),
        ),
    ]