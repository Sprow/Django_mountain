# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 09:29
from __future__ import unicode_literals

from django.db import migrations, models
import utils


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='city',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.FileField(upload_to=utils.get_file_path),
        ),
    ]
