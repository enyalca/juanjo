# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-17 09:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gprojects', '0051_auto_20160417_0926'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gtask',
            old_name='early_start',
            new_name='es',
        ),
        migrations.RemoveField(
            model_name='gtask',
            name='last_finish',
        ),
    ]
