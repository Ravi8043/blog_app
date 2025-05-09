from django.shortcuts import render
from .models import Blog
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.
class PostListView(ListView):
    model = Blog
    template_name = 'home.html'
    context_object_name = 'blogs'  


class PostDetailView(DetailView):
    model = Blog
    template_name = 'post_detail.html'
    context_object_name='blog'


class PostCreateView(CreateView):
    model=Blog
    template_name='post_new.html'
    fields=['title','content']

class PostEditView(UpdateView):
    model = Blog
    template_name = 'post_edit.html'
    fields=['title','content']
class PostDeleteView(DeleteView):
    model=Blog
    template_name='post_delete.html'
    success_url=reverse_lazy('home')
    