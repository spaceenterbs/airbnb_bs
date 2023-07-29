# Generated by Django 4.2.3 on 2023-07-29 04:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("experiences", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="experience",
            name="host",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="experience",
            name="perks",
            field=models.ManyToManyField(to="experiences.perk"),
        ),
    ]
