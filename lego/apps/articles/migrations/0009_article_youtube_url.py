# Generated by Django 2.1.7 on 2019-02-20 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("articles", "0008_remove_article_author")]

    operations = [
        migrations.AddField(
            model_name="article",
            name="youtube_url",
            field=models.CharField(default="", max_length=128),
        )
    ]
