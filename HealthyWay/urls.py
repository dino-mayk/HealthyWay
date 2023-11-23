from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path(
        '',
        include(
            'homepage.urls',
        ),
        name='homepage',
    ),
    path(
        'recipe/',
        include(
            'recipe.urls',
        ),
        name='recipe',
    ),
    path(
        'sport/',
        include(
            'sport.urls',
        ),
        name='sport',
    ),
    path(
        'mentalka/',
        include(
            'mentalka.urls',
        ),
        name='mentalka',
    ),
    path(
        'feedback/',
        include(
            'feedback.urls',
        ),
        name='feedback',
    ),
    path(
        'auth/',
        include(
            'user.urls',
        ),
        name='users',
    ),
    path(
        'tinymce/',
        include('tinymce.urls'),
        name='tinymce',
    ),
    path(
        'admin/',
        admin.site.urls,
        name='admin',
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
