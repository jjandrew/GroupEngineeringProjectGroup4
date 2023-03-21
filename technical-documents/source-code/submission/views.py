from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import ImageForm
from submission.models import ImageSubmission, RoomModel
from datetime import datetime, timedelta


@login_required
def submission_view(request):
    """ Displays the form (GET request) and takes the data from the form,
    validates it and awards the user points.
    """
    # Checks if request is after submitting form or before
    if request.method == 'POST':
        # Recreates the form with the posted data
        form = ImageForm(request.POST, request.FILES)

        # Checks the submission has all valid fields
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance

            # Get the username of the logged in user
            username = request.user.username
            # TODO: Different numbers of points for different rooms.
            # TODO: Add validation.

            return render(request, 'UI/submission.html',
                          {'form': form})
    else:
        # If not already submitted will create a new image form
        form = ImageForm()
    # Will return the formatted index.html file with the form entered
    return render(request, 'UI/submission.html', {'form': form})


@login_required
def working_submission_view(request):
    """ Displays the form (GET request) and takes the data from the form,
    validates it and awards the user points.
    """
    # Checks if request is after submitting form or before
    if request.method == 'POST':
        # Recreates the form with the posted data
        form = ImageForm(request.POST, request.FILES)

        # Checks the submission has all valid fields
        if form.is_valid():
            # Get the current instance object to display in the template

            # Gets the data from the form
            data = form.cleaned_data

            # Gets username of logged in user
            username = request.user.username

            # Create an image submission model of this
            image_submission = ImageSubmission(building=data["building"], room=data["room"],
                                               lights_status=data["lights_status"],
                                               windows_status=data["windows_status"],
                                               litter_items=data["litter_items"], image=data["image"],
                                               user=username, date=datetime.today().strftime('%Y-%m-%d'))

            # Check if a room has been submitted in the last hour
            # Get the room
            room = None
            skip = False
            if RoomModel.objects.filter(building=image_submission.building, name=image_submission.room.lower()).exists():
                room = RoomModel.objects.get(
                    name=image_submission.room.lower(), building=image_submission.building)
            else:
                skip = True
            if not skip:
                # Check if done an hour before
                hour_ago = (datetime.now() - timedelta(hours=1))
                if room.last_done.replace(tzinfo=None) > hour_ago:
                    return render(request, 'submission/index.html',
                                  {'form': form, 'message': "Error: room submitted too recently"})

            image_submission.save()

            # TODO VALIDATION HERE

            # TODO this is where gamekeeper validation occurs

            message = "Success"

            # TODO: Different numbers of points for different rooms.
            # TODO: Add validation.
            # points = calcPoints(image_submission.building)
            # addPoints(username, points)

            # Maybe reset the form?
            return render(request, 'submission/index.html',
                          {'form': form, 'message': message})
    else:
        # If not already submitted will create a new image form
        form = ImageForm()
    # Will return the formatted index.html file with the form entered
    return render(request, 'submission/index.html', {'form': form})
