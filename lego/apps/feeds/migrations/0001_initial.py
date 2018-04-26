# Generated by Django 2.0.3 on 2018-03-07 18:57

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models

import lego.apps.feeds.marker


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='NotificationFeed',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    )
                ),
                ('feed_id', models.CharField(db_index=True, max_length=64)),
                ('group', models.CharField(max_length=128)),
                ('activity_store', django.contrib.postgres.fields.jsonb.JSONField()),
                ('minimized_activities', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('seen_at', models.DateTimeField(null=True)),
                ('read_at', models.DateTimeField(null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, lego.apps.feeds.marker.MarkerModelMixin),
        ),
        migrations.CreateModel(
            name='PersonalFeed',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    )
                ),
                ('feed_id', models.CharField(db_index=True, max_length=64)),
                ('group', models.CharField(max_length=128)),
                ('activity_store', django.contrib.postgres.fields.jsonb.JSONField()),
                ('minimized_activities', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TimelineStorage',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    )
                ),
                ('activity_id', models.CharField(db_index=True, max_length=20)),
                ('feed', models.CharField(db_index=True, max_length=32)),
                ('aggregated_id', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserFeed',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    )
                ),
                ('feed_id', models.CharField(db_index=True, max_length=64)),
                ('group', models.CharField(max_length=128)),
                ('activity_store', django.contrib.postgres.fields.jsonb.JSONField()),
                ('minimized_activities', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='timelinestorage',
            unique_together={('activity_id', 'feed')},
        ),
    ]
