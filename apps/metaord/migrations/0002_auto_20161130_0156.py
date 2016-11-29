# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-29 22:56
from __future__ import unicode_literals
from django.db import migrations
from metaord.utils.auth import Groups


def add_group_permissions(apps, schema_editor):
    Groups.get_or_create_operator()
    Groups.get_or_create_boss()


class Migration(migrations.Migration):

    dependencies = [
        ('metaord', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_group_permissions)
    ]
