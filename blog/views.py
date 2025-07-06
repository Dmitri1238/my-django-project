from django.shortcuts import get_object_or_404, render
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})

def post_detail(request, id):
    # Получаем пост по ID или возвращаем 404, если не найден
    post = get_object_or_404(Post, pk=id)
    return render(request, 'blog/post_detail.html', {'post': post})