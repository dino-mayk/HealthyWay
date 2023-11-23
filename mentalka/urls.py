from django.urls import path

from mentalka import views

app_name = 'mentalka'

urlpatterns = [
    path(
        '',
        views.index,
        name='index',
    ),
]
