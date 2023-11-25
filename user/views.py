from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render

from user.forms import (
    CustomUserLoginForm,
    CustomUserSignUpForm,
    CustomUserProfileForm,
)


class Login(LoginView):
    form_class = CustomUserLoginForm


def signup(request):
    try:
        if request.method == 'POST':
            form = CustomUserSignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('homepage:index')

        else:
            form = CustomUserSignUpForm()

        return render(request, 'user/signup.html', {'form': form})
    except Exception:
        return redirect("user:signup")


@login_required
def profile(request):
    return render(request, 'user/profile.html')


@login_required
def settings(request):
    if request.method == 'POST':
        form = CustomUserProfileForm(
            data=request.POST,
            files=request.FILES,
            instance=request.user,
        )
        update = form.save(commit=False)
        update.user = request.user
        update.save()
    else:
        form = CustomUserProfileForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'user/settings.html', context)
