# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-18 16:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WishListApp1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishdata',
            old_name='num',
            new_name='wishnum',
        ),
    ]