# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 22:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("flatpages", "0001_initial")]

    operations = [
        migrations.RemoveField(model_name="page", name="level"),
        migrations.RemoveField(model_name="page", name="lft"),
        migrations.RemoveField(model_name="page", name="parent"),
        migrations.RemoveField(model_name="page", name="rght"),
        migrations.RemoveField(model_name="page", name="tree_id"),
    ]
