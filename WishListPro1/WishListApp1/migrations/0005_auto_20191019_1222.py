# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-19 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WishListApp1', '0004_remove_wishdata_wishnum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishdata',
            name='wishDatetobuy',
            field=models.DateField(blank=True, max_length=20, null=True),
        ),
    ]
