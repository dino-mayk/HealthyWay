from django.urls import path

from sport import views

app_name = 'sport'

urlpatterns = [
    path(
        '',
        views.index,
        name='index',
    ),
]
