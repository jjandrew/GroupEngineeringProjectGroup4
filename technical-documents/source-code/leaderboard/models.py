from django.db import models
from submission.models import building_choices
from datetime import datetime


class BuildingModel(models.Model):
    """A model for a room in order to calculate environmental statistics"""
    name = models.CharField(choices=building_choices, max_length=48)
    stats_since = models.DateField(
        default=datetime.today().strftime('%Y-%m-%d'))
    co2 = models.PositiveIntegerField(default=0)
