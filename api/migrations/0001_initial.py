# Generated by Django 4.2.4 on 2023-10-12 15:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Archive",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "streamer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(app_label)s_%(class)s",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["created_at"],
            },
        ),
        migrations.CreateModel(
            name="Save",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Video",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("video_id", models.SlugField(max_length=20)),
                (
                    "published_at",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("channel_id", models.SlugField(max_length=25)),
                ("title", models.CharField(max_length=250)),
                ("channel_title", models.CharField(max_length=50)),
                ("category_id", models.CharField(max_length=50)),
                ("duration", models.IntegerField(default=0)),
                ("dimension", models.CharField(max_length=50)),
                ("definition", models.CharField(max_length=50)),
                ("view_count", models.IntegerField(default=0)),
                ("like_count", models.IntegerField(default=0)),
                ("dislike_count", models.IntegerField(default=0)),
                ("favorite_count", models.IntegerField(default=0)),
                ("comment_count", models.IntegerField(default=0)),
                ("submitted_at", models.DateTimeField(auto_now_add=True)),
                ("submitted_by", models.CharField(max_length=50)),
                (
                    "archive",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(app_label)s_%(class)s",
                        to="api.archive",
                    ),
                ),
                (
                    "saves",
                    models.ManyToManyField(
                        through="api.Save", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            options={
                "ordering": ["-submitted_at"],
            },
        ),
        migrations.CreateModel(
            name="Thumbnail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "key",
                    models.CharField(
                        choices=[
                            ("default", "default"),
                            ("medium", "medium"),
                            ("high", "high"),
                            ("standard", "standard"),
                            ("maxres", "maxres"),
                        ],
                        max_length=10,
                    ),
                ),
                ("url", models.URLField(max_length=500)),
                ("height", models.IntegerField()),
                ("width", models.IntegerField()),
                (
                    "video",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(app_label)s_%(class)s",
                        to="api.video",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="save",
            name="video",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="api.video"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="save",
            unique_together={("video", "user")},
        ),
    ]
