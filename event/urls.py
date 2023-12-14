from django.urls import path

from event import views

app_name = 'event'

urlpatterns = [
    path(
        '',
        views.list,
        name='list',
    ),
    path(
        '<int:pk>/',
        views.detail,
        name='detail',
    ),
]
