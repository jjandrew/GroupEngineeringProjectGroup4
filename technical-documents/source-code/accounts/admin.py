""" Outlines the data to be used by the admins. """
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUser



class CustomUserAdmin(UserAdmin):
    """ Specifies the the sets of fields stored for every admin user,
    along with a list of which user metrics are displayed for them.

    Args:
        UserAdmin: The UserAdmin object representing the admin user.
    """
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'points',
    )

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('points',)
        })
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('points',)
        })
    )

admin.site.register(CustomUser, CustomUserAdmin)
