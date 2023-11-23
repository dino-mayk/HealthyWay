from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from user.forms import LoginForm

from user.forms import LoginForm
from user.models import CustomUser


class Login(LoginView):
    form_class = LoginForm


def signup(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            name = request.POST.get('name')
            surname = request.POST.get('surname')
            email = request.POST.get('email')
            password = request.POST.get('password')

            new_user = CustomUser.objects.create(
                username=username,
                name=name,
                surname=surname,
                email=email,
                password=password,
            )

            login(request, new_user)
            return redirect('homepage:index')

        return render(request, 'user/signup.html')
    except Exception:
        return redirect("user:signup")
