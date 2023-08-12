# Generated by Django 4.2.4 on 2023-08-12 08:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="twitchuser",
            name="broadcaster_type",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name="twitchuser",
            name="created_at",
            field=models.DateTimeField(default=datetime.datetime(2000, 1, 1, 0, 0)),
        ),
        migrations.AddField(
            model_name="twitchuser",
            name="profile_image_url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="twitchuser",
            name="type",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name="twitchuser",
            name="id",
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
