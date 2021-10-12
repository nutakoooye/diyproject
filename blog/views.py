from django.shortcuts import render
from .models import Post, Blogger, Comment


def index(request):

    num_bloggers = Blogger.objects.count()
    num_posts = Post.objects.count

    context = {
        'num_bloggers': num_bloggers,
        'num_posts': num_posts,
    }
    return render(request, 'index.html', context=context)
