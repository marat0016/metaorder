# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-29 22:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=512, blank=False)),
                ('email', models.EmailField(max_length=254, blank=False)),
                ('text', models.TextField()),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(max_length=128)),
            ],
        ),
    ]
