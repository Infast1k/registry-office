# Generated by Django 4.2.8 on 2023-12-20 14:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0014_alter_profile_birth_sertificate"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="birth_sertificate",
        ),
        migrations.DeleteModel(
            name="BirthSertificate",
        ),
    ]
