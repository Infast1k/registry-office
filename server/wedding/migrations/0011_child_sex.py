# Generated by Django 4.2.8 on 2023-12-20 15:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wedding", "0010_alter_child_options_children_address"),
    ]

    operations = [
        migrations.AddField(
            model_name="child",
            name="sex",
            field=models.CharField(default="мужчина", max_length=25),
            preserve_default=False,
        ),
    ]
