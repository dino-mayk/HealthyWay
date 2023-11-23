from django.urls import path

from feedback import views

app_name = 'feedback'

urlpatterns = [
    path(
        '',
        views.index,
        name='index',
    ),
    path(
        'done/',
        views.done,
        name='done',
    ),
]
