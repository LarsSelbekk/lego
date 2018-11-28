# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-30 13:36
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("companies", "0009_auto_20170928_1624")]

    operations = [
        migrations.AlterField(
            model_name="semesterstatus",
            name="contacted_status",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    choices=[
                        ("company_presentation", "company_presentation"),
                        ("course", "course"),
                        ("lunch_presentation", "lunch_presentation"),
                        ("bedex", "bedex"),
                        ("contact_in_oslo", "contact_in_oslo"),
                        ("interested", "interested"),
                        ("not_interested", "not_interested"),
                        ("contacted", "contacted"),
                        ("not_contacted", "not_contacted"),
                    ],
                    max_length=64,
                ),
                size=None,
            ),
        )
    ]
