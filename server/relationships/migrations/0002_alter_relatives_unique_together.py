# Generated by Django 4.2.8 on 2023-12-19 20:14

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("relationships", "0001_initial"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="relatives",
            unique_together={("user", "abstract_profile", "status")},
        ),
    ]
