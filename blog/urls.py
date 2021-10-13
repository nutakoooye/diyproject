from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogListView.as_view(), name='all-blogs'),
    path('bloggers/', views.BloggerListView.as_view(), name='all-bloggers'),
    path('<int:pk>/', views.BlogDetailView.as_view(), name='blog-detail'),
    path('blogger/<int:pk>', views.BloggerDetailView.as_view(), name='blogger-detail'),
    path('<int:pk>/comment', views.CommentCreate.as_view(), name='comment')
]