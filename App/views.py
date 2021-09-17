from django.shortcuts import render


def index(request):
    is_auth = request.user.is_authenticated
    
    context = {
        'is_auth': is_auth,
    }
    return render(request, 'App/index.html', context)
