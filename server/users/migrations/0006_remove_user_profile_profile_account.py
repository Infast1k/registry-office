# Generated by Django 4.2.6 on 2023-11-07 07:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_birthsertificate_pasport_profile_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profile',
        ),
        migrations.AddField(
            model_name='profile',
            name='account',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
