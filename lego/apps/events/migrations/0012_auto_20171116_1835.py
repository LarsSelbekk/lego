# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 18:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_auto_20171026_2043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='admin_reason',
            new_name='admin_registration_reason',
        ),
        migrations.AddField(
            model_name='registration',
            name='admin_unregistration_reason',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
