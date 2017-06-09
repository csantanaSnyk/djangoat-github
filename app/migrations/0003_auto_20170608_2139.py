# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-08 21:39
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='creator_id',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4294967295)]),
        ),
        migrations.AlterField(
            model_name='message',
            name='receiver_id',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4294967295)]),
        ),
    ]
