# Generated by Django 2.1.11 on 2020-02-12 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_user_selected_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='selected_theme',
            field=models.CharField(default='light', max_length=50, verbose_name='selected theme'),
        ),
    ]
