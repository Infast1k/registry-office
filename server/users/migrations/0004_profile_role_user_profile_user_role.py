# Generated by Django 4.2.6 on 2023-10-24 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_managers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=20)),
                ('patronymic', models.CharField(max_length=20, null=True)),
                ('sex', models.CharField(max_length=10)),
                ('birth_date', models.DateField()),
                ('phone', models.CharField(max_length=20, unique=True)),
                ('adress', models.CharField(max_length=100)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'role',
                'verbose_name_plural': 'roles',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='profile',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='users.role'),
        ),
    ]
