# Generated by Django 4.2.8 on 2023-12-20 15:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wedding", "0009_birthsertificate_child_childstatus_children"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="child",
            options={"verbose_name": "Child"},
        ),
        migrations.AddField(
            model_name="children",
            name="address",
            field=models.CharField(default="Ярославль", max_length=100),
            preserve_default=False,
        ),
    ]
