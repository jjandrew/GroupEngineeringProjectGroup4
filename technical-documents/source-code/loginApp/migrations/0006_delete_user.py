from django.db import migrations

class Migration(migrations.Migration):
    """ Defines the database migration for deleting a user from the database. 
    """
    dependencies = [
        ('loginApp', '0005_user_email_user_first_name_user_last_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
