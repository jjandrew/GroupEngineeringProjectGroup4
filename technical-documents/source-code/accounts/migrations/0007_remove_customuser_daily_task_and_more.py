# Generated by Django 4.1.5 on 2023-03-22 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_customuser_daily_task_customuser_last_daily_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='daily_task',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='last_daily_task',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='last_submission',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='streak',
        ),
    ]