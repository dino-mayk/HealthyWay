from django.urls import path

from recipe import views

app_name = 'recipe'

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
