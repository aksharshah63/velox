# Generated by Django 3.2.9 on 2022-05-31 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('velox_app', '0032_auto_20220531_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horse',
            name='broodmare_sire',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Broodmare Sire'),
        ),
        migrations.AlterField(
            model_name='horse',
            name='dam',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='horse',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='horse',
            name='sire',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
