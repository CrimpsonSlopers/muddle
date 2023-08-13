# Generated by Django 4.2.4 on 2023-08-13 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_delete_twitchuser"),
    ]

    operations = [
        migrations.CreateModel(
            name="Viewer",
            fields=[
                (
                    "login",
                    models.CharField(max_length=250, primary_key=True, serialize=False),
                ),
                ("muted", models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterModelOptions(
            name="streamsession",
            options={"ordering": ["created_at"]},
        ),
    ]