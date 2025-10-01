from sqlite3 import IntegrityError
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
                'error': 'Wrong user or password!'
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
        data = {
            'first_name': request.POST.get('first_name', '').strip(),
            'last_name':  request.POST.get('last_name', '').strip(),
            'email':      request.POST.get('email', '').strip(),
            'username':   request.POST.get('username', '').strip(),
            'password':   request.POST.get('password', ''),
        }

        errors = {}
        if not data['username']:
            errors['username'] = 'User is needed.'
        if not data['email']:
            errors['email'] = 'Email is needed.'
        if not data['password']:
            errors['password'] = 'The password is needed.'

        if User.objects.filter(username=data['username']).exists():
            errors['username'] = 'User already exists.'
        if User.objects.filter(email=data['email']).exists():
            errors['email'] = 'Email already exists.'

        if errors:
            return render(request, 'users/signup.html', {'errors': errors, 'data': data})

        try:
            user = User.objects.create_user(
                username=data['username'],
                email=data['email'],
                password=data['password'],
                first_name=data['first_name'],
                last_name=data['last_name'],
            )
        except IntegrityError:
            return render(request, 'users/signup.html', {
                'errors': {'username': 'Username already exists.'},
                'data': data,
            })

        auth_user = authenticate(username=data['username'], password=data['password'])
        login(request, auth_user)
        return redirect('users:profile')

    return render(request, 'users/signup.html')