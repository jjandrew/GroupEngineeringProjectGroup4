# Generated by Django 4.1.5 on 2023-02-26 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0003_rename_turner off plug sockets?_imagesubmission_turned off plug sockets?'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagesubmission',
            old_name='Removed Litter?',
            new_name='no_litter',
        ),
        migrations.RenameField(
            model_name='imagesubmission',
            old_name='Turned off Plug Sockets?',
            new_name='sockets_off',
        ),
    ]