# Generated by Django 3.2.9 on 2021-12-10 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('velox_app', '0008_auto_20211210_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='measure',
            name='biomechanics_operation_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='measure',
            name='biomechanics_video_probability',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='measure',
            name='biomechanics_video_score',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
