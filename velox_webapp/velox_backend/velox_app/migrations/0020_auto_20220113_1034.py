# Generated by Django 3.2.9 on 2022-01-13 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('velox_app', '0019_auto_20220112_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measure',
            name='cardio_type',
            field=models.CharField(blank=True, choices=[('Bullseye', 'Bullseye'), ('Turf/Off-speed Dirt', 'Turf/Off-speed Dirt'), ('Irregular/Immature', 'Irregular/Immature'), ('Small/Sprint', 'Small/Sprint')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='measure',
            name='video_qc',
            field=models.CharField(blank=True, choices=[('Poor', 'Poor'), ('OK', 'OK'), ('Good', 'Good')], max_length=20, null=True),
        ),
    ]
