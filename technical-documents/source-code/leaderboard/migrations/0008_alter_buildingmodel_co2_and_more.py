# Generated by Django 4.1.5 on 2023-03-22 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0007_merge_20230322_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buildingmodel',
            name='co2',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='buildingmodel',
            name='stats_since',
            field=models.DateField(default='2023-03-22'),
        ),
    ]
