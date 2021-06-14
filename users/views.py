from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def register(request):

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'Account created for {username}!')
            return redirect('users:login')

    else:
        form = UserRegistrationForm()
    return render(request, "users/register.html", {"form": form})



