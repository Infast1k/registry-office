# Generated by Django 4.2.8 on 2023-12-15 14:47

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0012_alter_user_role"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("wedding", "0004_rename_event_datatime_wedding_event_datetime"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="wedding",
            options={"verbose_name": "wedding", "verbose_name_plural": "weddings"},
        ),
        migrations.AlterUniqueTogether(
            name="wedding",
            unique_together={("user", "profile")},
        ),
    ]
