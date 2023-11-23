from django.contrib.auth.views import LogoutView
from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path(
        'signup/',
        views.signup,
        name='signup',
    ),
    path(
        'login/',
        views.Login.as_view(
            template_name='user/login.html',
        ),
        name='login',
    ),
    path(
        'logout/',
        LogoutView.as_view(
            template_name='user/logout.html',
        ),
        name='logout',
    ),
]
