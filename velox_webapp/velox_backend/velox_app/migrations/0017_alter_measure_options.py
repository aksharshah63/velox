# Generated by Django 3.2.9 on 2022-01-05 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('velox_app', '0016_auto_20220105_1419'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='measure',
            options={'ordering': ['id']},
        ),
    ]
