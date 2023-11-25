from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.safestring import mark_safe
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete, get_thumbnail


class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=150,
    )
    name = models.CharField(
        max_length=150,
    )
    surname = models.CharField(
        max_length=150,
    )
    email = models.EmailField(
        'email',
        unique=True,
    )
    """weight = models.IntegerField(
        blank=True,
        null=True,
    )
    height = models.IntegerField(
        blank=True,
        null=True,
    )
    age = models.IntegerField(
        blank=True,
        null=True,
    )
    GENDER_TYPES = [
        (True, 'Мужчина'),
        (False, 'Женщина'),
    ]
    gender = models.BooleanField(
        choices=GENDER_TYPES,
        blank=True,
        null=True,
    )
    avatar = models.ImageField(
        upload_to='uploads/avatars/%Y/%m',
        verbose_name='аватар',
        help_text='загрузите картинку',
        default='default_avatar.jpg',
    )"""
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username',
    ]

    @property
    def get_img(self):
        return get_thumbnail(self.avatar, '300x300', crop='center', quality=51)

    def img_tmb(self):
        if self.avatar:
            return mark_safe(
                f'<img src="{self.get_img.url}">'
            )
        return 'нет изображений'

    img_tmb.short_description = 'превьюшки'
    img_tmb.allow_tags = True

    def sorl_delete(**kwargs):
        delete(kwargs['file'])

    cleanup_pre_delete.connect(sorl_delete)

    def __str__(self):
        return f'{self.email}'
