""" Outlines the functions required by the homepage app. """
import random
from datetime import date
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def get_daily_task(user):
    """ Get's the user's daily task.

    Args:
        user: User: The user object for which to calculate the daily task for.
    """

    # Check if the user has a daily task assigned for today
    if user.last_daily_task != date.today():
        # Generate a new daily task and assign it to the user

        user.daily_task = random.randint(0, 43)  # 44 options
        user.last_daily_task = date.today()
        user.save()


@login_required
def index(request):
    """ The base homepage that is displayed to the user.

    Args:
        request: The HTTP request submitted by the user.

    Return: render(): Displays the homepage, along with each of the required
        fields, to the user.
    """
    user = request.user

    get_daily_task(user)

    building_choices = ['Alexander',
                        'Amory',
                        'Business School Building:One',
                        'Byrne House',
                        'Clayden',
                        'Clydesdale House',
                        'Cornwall House',
                        'Cornwall House Swimming Pool',
                        'Devonshire House',
                        'Estate Service Centre',
                        'Family Centre (Owlets)',
                        'Forum and Library',
                        'Geoffrey Pope',
                        'Great Hall and University Reception',
                        'Harrison',
                        'Hatherly',
                        'Henry Wellcome Building for Biocatalysis',
                        'Innovation Centre Phase 1 and 2', 'Institute of Arab and Islamic Studies',
                        'INTO International Study Centre',
                        'Kay House Duryard', 'Knightley',
                        'Lafrowda House',
                        'Laver',
                        'Lazenby',
                        'Mary Harris Memorial Chapel',
                        'Newman',
                        'Northcote House',
                        'Northcott Theatre',
                        'Old Library',
                        'Peter Chalk Centre',
                        'Physics',
                        "Queen's",
                        'Redcot',
                        'Reed Hall',
                        'Reed Mews Wellbeing Centre',
                        'Roborough',
                        'Russell Seal Fitness Centre',
                        'Sir Christopher Ondaatje Devon Cricket Centre',
                        'Sir Henry Wellcome Building for Mood Disorders Research',
                        'Streatham Court',
                        'Streatham Farm',
                        'Washington Singer',
                        'Xfi']

    # Extracts the user's daily task
    task_number = user.daily_task
    task = building_choices[task_number]

    # Extracts each of the user's data points

    username = request.user.username
    email = request.user.email
    points = request.user.points
    streak = request.user.streak

    args = {'username': username, 'email': email,
            'points': points, 'streak': streak, 'task': task}
    return render(request, "homepage/homepage.html", args)
