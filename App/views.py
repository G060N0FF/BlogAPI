from django.shortcuts import render


def index(request):
    context = {
        'is_auth': request.user.is_authenticated,
        'user': request.user,
    }
    return render(request, 'App/index.html', context)
