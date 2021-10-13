from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Post, Blogger, Comment
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

def index(request):
    num_bloggers = Blogger.objects.count()
    num_posts = Post.objects.count

    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    context = {
        'num_bloggers': num_bloggers,
        'num_posts': num_posts,
        'num_visits': num_visits,
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





class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['message']
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return super(CommentCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CommentCreate, self).get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, pk=self.kwargs['pk'])
        return context


    def get_success_url(self):

        return reverse('blog-detail', kwargs={'pk': self.kwargs['pk'],})




