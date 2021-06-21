from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Post
from django.core.paginator import Paginator
from django.urls import reverse_lazy
# Create your views here.

class PostListView(ListView):
    model = Post
    paginate_by = 11
    template_name = "people/post_list.html"

class PostCreateView(CreateView):
    model = Post
    template_name = "people/post_create.html"
    success_url = reverse_lazy("post_list")

class PostUpdateView(UpdateView):
    model = Post

class PostDeleteView(DeleteView):
    model = Post
    template_name = "todos/delete_date.html"
    success_url = reverse_lazy("post_list")