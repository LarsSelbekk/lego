# Generated by Django 2.2.13 on 2020-10-27 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0027_registration_payment_idempotency_key"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="use_contact_tracing",
            field=models.BooleanField(default=False),
        ),
    ]
