""" Creates all the forms to be displayed to the user as part of the signup
app.
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser


class SignUpForm(UserCreationForm):
    """ Defines the parameters and data collected from the sign up form,
    in addition to methods for cleaning and validating the username, email and
    password.

    Args:
        UserCreationForm: The Django default form object for creating users.
    """
    def __init__(self, *args, **kwargs):
        """ The constructor for the signup form that specifies the CSS characteristics for
        both the username, first name, last name, email and password fields.
        """
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'un',
            'type': 'text',
            'align': "center",
            'name': 'username',
            'placeholder': 'Username',

        })
        self.fields['email'].widget.attrs.update({
            'class': 'un',
            'type': 'email',
            'align': "center",
            'name': 'email',
            'placeholder': 'email@exeter.ac.uk',
        })
        self.fields['first_name'].widget.attrs.update({
            'class': 'un',
            'type': 'text',
            'align': "center",
            'name': 'first_name',
            'placeholder': 'Name',
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'un',
            'type': 'text',
            'align': "center",
            'name': 'last_name',
            'placeholder': 'Surname',
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'pass',
            'type': 'password',
            'align': "center",
            'name': 'password1',
            'placeholder': 'Password',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'pass',
            'type': 'password',
            'align': "center",
            'name': 'password2',
            'placeholder': 'Confirm password',
        })
    # Each of the fields to be displayed on the signup page
    username = forms.CharField(max_length=20, label=False)
    first_name = forms.CharField(max_length=20, label=False)
    last_name = forms.CharField(max_length=20, label=False)
    email = forms.EmailField(max_length=100)

    def clean_email(self):
        """ Validates the email the user enters into the sign up form to ensure
        it is an @exeter.ac.uk email.

        Return:
            str: cleanEmail: The 'cleaned' version of the email the user
                entered into the signup page, given as a string for ease of
                processing.
        """
        clean_email = self.cleaned_data['email']

        if "@exeter.ac.uk" not in clean_email:
            raise forms.ValidationError("Please use an @exeter.ac.uk email.")

        return clean_email

    def clean_password2(self):
        """ 'Cleans' the passwords entered into the form and checks if they
        match, raising an error if they don't.

        Return:
            str: password: The second password the user entered into the signup
                page, returned as a string for ease of processing.
        """
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        # Ensures both password boxes are filled
        if password1 and password2:

            if password1 != password2:
                raise forms.ValidationError("Passwords do not match.")

        return password2


    def clean_username(self):
        """ 'Cleans' the username entered into the form and checks that the
        username the user has entered is unique.

        Returns:
            str: username: Returns the name of the user as a string for ease
                of processing.
        """
        username = self.cleaned_data['username']

        try:
            user = CustomUser.objects.exclude(pk=self.instance.pk).get(username=username)

        except CustomUser.DoesNotExist:
            return username

        # Throws an error if the username is already being used
        raise forms.ValidationError(f'Username {username} is already in use.')

    class Meta:
        """ A class that talks about the sign up class, enabling further
        validators to be created.
        """
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2',)
