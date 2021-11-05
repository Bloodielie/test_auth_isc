from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import FormView

from . import forms


@login_required
def profile(request):
    return render(request, "auth/profile.html")


class LoginView(FormView):
    template_name = 'registration/login.html'
    form_class = forms.LoginForm

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password')
        try:
            user = User.objects.get(username=username)
            if user.check_password(raw_password):
                login(self.request, user)
                return redirect("profile")

            form.add_error("password", "Invalid login or password")
        except ObjectDoesNotExist:
            form.add_error("password", "Invalid login or password")

        return render(self.request, 'registration/login.html', {'form': form})

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("profile")

        return super().dispatch(request, *args, **kwargs)


class SignUpView(FormView):
    template_name = 'registration/signup.html'
    form_class = forms.SignUpForm

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return redirect("profile")
