from django.urls import path
from . import views
from django.views.generic import ListView, DetailView
from .models import Post
urlpatterns = [
    path('', ListView.as_view(
        queryset = Post.objects.all().order_by("-createAt"),
        template_name = 'blog/blog.html',
        context_object_name = 'Posts',
        paginate_by = 10)
        , name='blog'),
    path('<int:pk>/', views.post , name='post'),#blog/id
    path('manage/', views.list),
    path('manage/create', views.newPost, name='create'),
    path('manage/update/<str:pk>', views.updatePost, name='update'),
    path('manage/delete/<str:pk>', views.deletePost, name='delete'),
    path('search/', views.search, name='search')
]

