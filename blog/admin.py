from django.contrib import admin
from .models import Blogger, Post, Comment

#admin.site.register(Post)
admin.site.register(Blogger)
admin.site.register(Comment)


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'blogger', 'date_add')
    list_filter = ('date_add',)
    inlines = [CommentInline]





