# Generated by Django 5.0.2 on 2024-03-28 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_customuseradmin'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUserAdmin',
        ),
    ]