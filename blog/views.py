from django.shortcuts import render
from .models import Post, Blogger, Comment
from django.views import generic


def index(request):
    num_bloggers = Blogger.objects.count()
    num_posts = Post.objects.count

    context = {
        'num_bloggers': num_bloggers,
        'num_posts': num_posts,
    }
    return render(request, 'index.html', context=context)


class BlogListView(generic.ListView):
    model = Post
    paginate_by = 5

class BloggerListView(generic.ListView):
    model = Blogger


class BloggerDetailView(generic.DetailView):
    model = Blogger


class BlogDetailView(generic.DetailView):
    model = Post
