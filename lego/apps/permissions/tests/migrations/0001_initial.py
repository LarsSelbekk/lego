# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 10:44
from __future__ import unicode_literals

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("users", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="TestModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        db_index=True, default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "deleted",
                    models.BooleanField(db_index=True, default=False, editable=False),
                ),
                (
                    "require_auth",
                    models.BooleanField(default=False, verbose_name="require auth"),
                ),
                ("name", models.CharField(max_length=30, verbose_name="name")),
                (
                    "can_edit_groups",
                    models.ManyToManyField(
                        blank=True,
                        related_name="can_edit_testmodel",
                        to="users.AbakusGroup",
                    ),
                ),
                (
                    "can_edit_users",
                    models.ManyToManyField(
                        blank=True,
                        related_name="can_edit_testmodel",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "can_view_groups",
                    models.ManyToManyField(
                        blank=True,
                        related_name="can_view_testmodel",
                        to="users.AbakusGroup",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        default=None,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="testmodel_created",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        default=None,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="testmodel_updated",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"abstract": False, "default_manager_name": "objects"},
        )
    ]
