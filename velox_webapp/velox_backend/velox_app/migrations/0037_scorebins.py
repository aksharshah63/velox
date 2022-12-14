# Generated by Django 3.2.9 on 2022-07-16 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('velox_app', '0036_mlmodelmetadata'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScoreBins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('prob_field_name', models.CharField(max_length=100)),
                ('bins', models.JSONField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
