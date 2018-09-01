from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .models import Post
from .forms import PostForm

def post_list(requset):
    qs = Post.objects.all()
    qs = qs.filter(published_date__lte=timezone.now())
    qs = qs.order_by('published_date')

    return render(requset, 'blog/post_list.html', {
        'post_list' : qs,
    })

def post_detail(requset, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(requset, 'blog/post_detail.html', {
        'post' : post
    })

def post_new(requset):
    if requset.method == 'POST':
        form = PostForm(requset.POST, requset.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post.pk)
    else:
        form = PostForm()

    return render(requset, 'blog/post_new.html', {
        'form' : form,
    })

def post_edit(requset, pk):
    post = get_object_or_404(Post, pk=pk)

    if requset.method == 'POST':
        form = PostForm(requset.POST, requset.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post.pk)
    else:
        form = PostForm(instance=post)

    return render(requset, 'blog/post_edit.html', {
        'form' : form,
    })