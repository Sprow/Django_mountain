# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-13 10:59
from __future__ import unicode_literals

from django.db import migrations, models
import utils


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20170413_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websitesettings',
            name='favicon',
            field=models.FileField(blank=True, null=True, upload_to=utils.get_file_path),
        ),
    ]
