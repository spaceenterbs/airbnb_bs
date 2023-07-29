# Generated by Django 4.2.3 on 2023-07-29 09:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("experiences", "0002_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("rooms", "0003_remove_amenity_category_room_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="Wishlist",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=150)),
                ("experiences", models.ManyToManyField(to="experiences.experience")),
                ("rooms", models.ManyToManyField(to="rooms.room")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
