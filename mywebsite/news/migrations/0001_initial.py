# Generated by Django 5.1.7 on 2025-05-07 02:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("title", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="NewsUnit",
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
                ("author", models.CharField(max_length=20)),
                ("title", models.CharField(max_length=100)),
                ("content", models.TextField()),
                ("pub_date", models.DateTimeField(auto_now_add=True)),
                ("is_show", models.BooleanField(default=False)),
                ("click_count", models.IntegerField(default=0)),
                ("image", models.ImageField(null=True, upload_to="news_images/")),
                ("link", models.URLField(null=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="news.category"
                    ),
                ),
            ],
        ),
    ]
