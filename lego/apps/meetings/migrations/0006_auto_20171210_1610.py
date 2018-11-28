# Generated by Django 2.0 on 2017-12-10 16:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("meetings", "0005_auto_20171026_2020")]

    operations = [
        migrations.AlterField(
            model_name="meeting",
            name="created_by",
            field=models.ForeignKey(
                default=None,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="meeting_created",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="meeting",
            name="report_author",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="meetings_reports",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="meeting",
            name="updated_by",
            field=models.ForeignKey(
                default=None,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="meeting_updated",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="meetinginvitation",
            name="created_by",
            field=models.ForeignKey(
                default=None,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="meetinginvitation_created",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="meetinginvitation",
            name="updated_by",
            field=models.ForeignKey(
                default=None,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="meetinginvitation_updated",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
