from gc import get_objects
from typing import OrderedDict
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post
from . import models
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User

def home(request):
    context={
        'posts':Post.objects.all()
        
    }
    return render(request,'blog/home.html',context)


class PostListView(ListView):
    template_name='blog/home.html'    
    context_object_name='posts'
    queryset=Post.objects.all()
    ordering=['-date_posted']
    paginate_by= 4
    
class PostDetailView(DetailView):
    model=Post
    context_object_name='posts'

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','content']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url='/'
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        else:
            return False
        
    

class filterListView(ListView):
    template_name='blog/filter.html'    
    context_object_name='posts'
    paginate_by= 4
    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('name'))
        return Post.objects.filter(author=user)

def about(request):
    return render(request,'blog/about.html',{'title':'blog'})