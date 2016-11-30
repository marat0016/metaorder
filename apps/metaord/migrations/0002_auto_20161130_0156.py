# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-29 22:56
from __future__ import unicode_literals
from django.db import migrations
from django.contrib.auth.models import User
from metaord.utils.auth import Groups
from metaord.models import Order
from metaord import settings


def add_group_permissions(apps, schema_editor):
    Groups.get_or_create_worker()
    Groups.get_or_create_chief()
    
    if settings.DEBUG:
        t1 = User.objects.create_user('t1', 'c@b.ru', '123')
        t1.groups.add(Groups.get_or_create_worker())
        t2 = User.objects.create_user('t2', 'd@b.ru', '123')
        t2.groups.add(Groups.get_or_create_chief())

        Order.objects.create(author='test1', email='a@b.ru', text='testing1')
        Order.objects.create(author='test2', email='b@c.ru', text='testing2')


class Migration(migrations.Migration):

    dependencies = [
        ('metaord', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_group_permissions)
    ]
