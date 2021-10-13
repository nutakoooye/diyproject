from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Blogger(models.Model):

    name = models.CharField(max_length=255)
    bio = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blogger-detail', args=[str(self.id)])


class Post(models.Model):

    title = models.CharField(max_length=255)
    content = models.TextField()
    date_add = models.DateField(auto_now_add=True)
    blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_add']
        permissions = (('can_create_new_post', 'Can create new post'),)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])


class Comment(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author

    class Meta:
        ordering = ['date_add']

