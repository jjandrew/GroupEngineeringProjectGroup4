""" Creates the class for creating a building leaderboard. """
from django.db import migrations, models


class Migration(migrations.Migration):
    """ Defines the database migration for creating the building leaderboard
    model, including the range of buildings.

    Args:
        migrations.Migration (Migration): The type of migrations to be applied
            on the database.
    """
    initial = True

    dependencies = [
        ('leaderboard', '0002_delete_leaderboard'),
    ]

    operations = [
        # Operations for creating the name and id fields for the leadeboard
        migrations.CreateModel(
            name='BuildingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('name',
                 models.CharField(choices=[('ALEXANDER', 'Alexander'),
                                            ('AMORY', 'Amory'),
                                            ('BUSINESSSCHOOLBUILDINGONE',
                                             'Business School Building:One'),
                                            ('BYRNEHOUSE', 'Byrne House'),
                                            ('CLAYDEN', 'Clayden'),
                                            ('CLYDESDALEHOUSE', 'Clydesdale House'),
                                            ('CORNWALLHOUSE', 'Cornwall House'),
                                            ('CORNWALLHOUSESWIMMINGPOOL',
                                             'Cornwall House Swimming Pool'),
                                            ('DEVONSHIREHOUSE', 'Devonshire House'),
                                            ('ESTATESERVICECENTRE', 'Estate Service Centre'),
                                            ('FAMILYCENTREOWLETS', 'Family Centre (Owlets)'),
                                            ('FORUMANDLIBRARY', 'Forum and Library'),
                                            ('GEOFFREYPOPE', 'Geoffrey Pope'),
                                            ('GREATHALLANDUNIVERSITYRECEPTION',
                                             'Great Hall and University Reception'),
                                            ('HARRISON', 'Harrison'),
                                            ('HATHERLY', 'Hatherly'),
                                            ('HENRYWELLCOMEBUILDINGFORBIOCATALYSIS',
                                             'Henry Wellcome Building for Biocatalysis'),
                                            ('INNOVATIONCENTREPHASE1AND2',
                                             'Innovation Centre Phase 1 and 2'),
                                            ('INSTITUTEOFARABANDISLAMICSTUDIES',
                                             'Institute of Arab and Islamic Studies'),
                                            ('INTOINTERNATIONALSTUDYCENTRE',
                                             'INTO International Study Centre'),
                                            ('KAYHOUSEDURYARD', 'Kay House Duryard'),
                                            ('KNIGHTLEY', 'Knightley'),
                                            ('LAFROWDAHOUSE', 'Lafrowda House'),
                                            ('LAVER', 'Laver'),
                                            ('LAZENBY', 'Lazenby'),
                                            ('MARYHARRISMEMORIALCHAPEL',
                                             'Mary Harris Memorial Chapel'),
                                            ('NEWMAN', 'Newman'),
                                            ('NORTHCOTEHOUSE', 'Northcote House'),
                                            ('NORTHCOTTTHEATRE', 'Northcott Theatre'),
                                            ('OLDLIBRARY', 'Old Library'),
                                            ('PETERCHALKCENTRE', 'Peter Chalk Centre'),
                                            ('PHYSICS', 'Physics'),
                                            ('QUEENS', "Queen's"),
                                            ('REDCOT', 'Redcot'),
                                            ('REEDHALL', 'Reed Hall'),
                                            ('REEDMEWSWELLBEINGCENTRE',
                                             'Reed Mews Wellbeing Centre'),
                                            ('ROBOROUGH', 'Roborough'),
                                            ('RUSSELLSEALFITNESSCENTRE',
                                             'Russell Seal Fitness Centre'),
                                            ('SIRCHRISTOPHERONDAATJEDEVONCRICKETCENTRE',
                                             'Sir Christopher Ondaatje Devon Cricket Centre'),
                                            ('SIRHENRYWELLCOMEBUILDINGFORMOODDISORDERSRESEARCH',
                                             'Sir Henry Wellcome Building' +
                                             ' for Mood Disorders Research'),
                                            ('STREATHAMCOURT', 'Streatham Court'),
                                            ('STREATHAMFARM', 'Streatham Farm'),
                                            ('WASHINGTONSINGER', 'Washington Singer'),
                                            ('XFI', 'Xfi')], max_length=48)),
                ('stats_since', models.DateField(default='2023-03-19')),
                ('co2', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
