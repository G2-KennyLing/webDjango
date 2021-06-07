from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comment
from blog.forms import CommentForm, PostForm
from django.http import HttpResponseRedirect
from .models import Post
from django.views import generic
from django.db.models import Q 
import operator

# Create your views here.
def post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST,author=request.user,post=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request, "blog/post.html", {"post":post, "form":form})
def list(request):
    Data = {'Posts': Post.objects.all().order_by("-createAt")}
    return render(request, "blog/manage.html", Data)
def newPost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect("/blog/manage")
    return render(request, "blog/createPost.html", {'form':form})
def updatePost(request, pk):
    post = Post.objects.get(id = pk)
    form = PostForm(instance= post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance= post)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect("/blog/manage")
    return render(request, "blog/createPost.html", {'form':form})
def deletePost(request, pk):
    post = Post.objects.get(id = pk)
    post.delete()
    return HttpResponseRedirect("/blog/manage")

def search(request):
    query = request.GET.get('q')
    if query:

        Data = {'Posts':Post.objects.filter(Q(title__icontains=query) | Q(body__icontains=query)).order_by("-createAt").distinct()}
        print(Data)
        return render(request, "blog/blog.html", Data)
    else:
        Data = {'Posts': Post.objects.all().order_by("-createAt")} 
        return render(request, "blog/blog.html", Data)
