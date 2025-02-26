# Generated by Django 4.2.6 on 2023-10-30 13:16

from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_role_user_profile_user_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='BirthSertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_place', models.CharField(max_length=100)),
                ('place_of_birth', models.CharField(max_length=100)),
                ('vital_record', models.PositiveIntegerField(unique=True)),
            ],
            options={
                'verbose_name': 'birth sertificate',
                'verbose_name_plural': 'birth sertificates',
            },
        ),
        migrations.CreateModel(
            name='Pasport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numbers', models.PositiveIntegerField(unique=True)),
                ('series', models.PositiveIntegerField(unique=True)),
                ('registration_place', models.CharField(max_length=100)),
                ('created_at', models.DateField()),
            ],
            options={
                'verbose_name': 'pasport',
                'verbose_name_plural': 'pasports',
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='Image',
            field=models.ImageField(null=True, upload_to=users.models.user_directory_path),
        ),
        migrations.AddField(
            model_name='profile',
            name='birth_sertificate',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.birthsertificate'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='pasport',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.pasport'),
            preserve_default=False,
        ),
    ]
