from django.shortcuts import render, redirect, reverse
from .forms import RegisterForm
from verify_email.email_handler import send_verification_email
from django.contrib.auth.models import User
from main import views as mv
from django.contrib.auth.views import LoginView


# Create your views here.
from .models import Profile


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            p = Profile.objects.get_or_create(user=user, profesion=form.cleaned_data['profesion'], cui=form.cleaned_data['cui'])
            return redirect(reverse('profile', kwargs={'nom':user.username}))

    else:
        form = RegisterForm()

    return render(request, 'registro/registro.html', {'form':form})


class Inicio(LoginView):

    def get_new_url(self):

        return str(self.request.user)