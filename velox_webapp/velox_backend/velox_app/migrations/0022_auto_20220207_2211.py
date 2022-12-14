# Generated by Django 3.2.9 on 2022-02-07 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('velox_app', '0021_auto_20220207_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horse',
            name='race_rating',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='horse',
            name='starts',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='horse',
            name='status',
            field=models.CharField(choices=[('Live', 'Live'), ('Retired', 'Retired'), ('Unraced', 'Unraced'), ('Unnamed', 'Unnamed')], default='Unnamed', max_length=10),
        ),
        migrations.AlterField(
            model_name='measure',
            name='horse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measures', to='velox_app.horse'),
        ),
    ]
