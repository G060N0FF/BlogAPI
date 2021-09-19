from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogPostForm


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


@login_required
def create_blog_post(request):
    form = BlogPostForm()

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            new_blog = form.save()
            new_blog.user = request.user
            new_blog.save()
            return redirect('/blog/' + str(new_blog.pk))

    context = {'form': form}
    return render(request, 'App/create_blog_post.html', context)


def blog(request, id):
    blog = BlogPost.objects.get(pk=id)

    context={'blog': blog}
    return render(request, 'App/blog.html', context)
