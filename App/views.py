from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def index(request):
    context = {
        'is_auth': request.user.is_authenticated,
        'user': request.user,
    }
    return render(request, 'App/index.html', context)


def sign_up(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')

    context = {'form': form}
    return render(request, 'registration/sign_up.html', context)
