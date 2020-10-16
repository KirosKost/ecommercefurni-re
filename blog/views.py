from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from . models import Post


def design(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'blog/ideas.html', context)
