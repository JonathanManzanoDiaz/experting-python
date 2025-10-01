from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from blog.models import Post
from django.contrib.auth.models import User
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('users:profile')
        else:
            return render(request, 'users/login.html', {
                'error': 'Usuario o contraseña incorrectos'
            })
    return render(request, 'users/login.html')

@login_required
def profile(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'users/profile.html', {
        'posts': posts,
    })

@login_required
def logout_view(request):
    logout(request)
    return redirect('posts:index')


def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect('users:profile')
    return render(request, 'users/signup.html')