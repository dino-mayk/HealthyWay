from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)

from user.models import CustomUser


class CustomUserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'


class CustomUserSignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            'username',
            'name',
            'surname',
            'email',
        )
        labels = {
            CustomUser.username.field.name: 'Никнейм',
            CustomUser.name.field.name: 'Имя',
            CustomUser.surname.field.name: 'Фамилия',
            CustomUser.email.field.name: 'Электронная почта',
        }


class CustomUserProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'name',
            'surname',
            "email"
        )
        labels = {
            CustomUser.username.field.name: 'Никнейм',
            CustomUser.name.field.name: 'Имя',
            CustomUser.surname.field.name: 'Фамилия',
            CustomUser.email.field.name: 'Электронная почта',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'
