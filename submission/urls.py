from django.urls import path

from . import views

urlpatterns = [
    path('', views.submission_view, name='submission'),
]