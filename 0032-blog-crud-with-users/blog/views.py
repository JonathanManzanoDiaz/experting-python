from django.shortcuts import get_object_or_404, redirect, render
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {
        'posts': posts,
    })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {
        'post':post,
    })
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.user != post.author and not request.user.is_superuser:
        return redirect('posts:post_detail', pk=post.pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html', {
        'form': form,
    })

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:post_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'blog/create_post.html', {'form': form})

@login_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from blog.models import Post

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.user != post.author and not request.user.is_superuser:
        return redirect('posts:post_detail', pk=post.pk)

    post.delete()
    return redirect('posts:index')