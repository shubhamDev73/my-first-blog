from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def post_list(request):
    posts = Post.objects.order_by('-created_date')
    return render(request, 'blogs/post_list.html', {'posts':posts})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blogs/post_detail.html', {'post': post})
@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        return render(request, 'blogs/post_new.html', {'FOrm': form})
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.edited_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        return render(request, 'blogs/post_new.html', {'FOrm': form})
@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')
def signup(request):
    if request.method == 'POST':
        userName = request.POST.get('username', None)
        password = request.POST.get('password', None)
        email = request.POST.get('email', None)
        try:
            obj = User.objects.get(username=userName)
        except User.DoesNotExist:
            if userName == '' or password == '':
                return render(request, 'registration/signup.html', {'error': 'Some required fields are empty'})
            else:
                user = User.objects.create_user(userName, email, password)
                user.save()
                login(request, user)
                return redirect('post_list')
        return render(request, 'registration/signup.html', {'error':'User already exists'})
    else:
        return render(request, 'registration/signup.html')
def signup_end(request):
    return render(request, 'registration/signup_end.html')
