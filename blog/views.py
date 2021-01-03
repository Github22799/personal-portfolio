from django.shortcuts import render, get_object_or_404
from .models import Post

def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/all_posts.html', { 'posts': posts })

def post(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'blog/post.html', { 'post':post })
