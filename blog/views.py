from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from .models import Post

# Create your views here.

# List of blogs
class BlogListView(ListView):

    model = Post

    template_name = 'home.html'

# Detail of each blogs
class BlogDetailView(DetailView):

    model = Post

    template_name = 'post_detail.html'

# Create new blog by user
class BlogCreateView(CreateView):

    model = Post

    template_name = 'post_new.html'

    fields = '__all__'

# Update blog post
class BlogUpdateView(UpdateView):

    model = Post

    template_name = 'post_edit.html'

    fields = ['title', 'body']

# Delete blog post
class BlogDeleteView(DeleteView):

    model = Post

    template_name = 'post_delete.html'

    success_url = reverse_lazy('home')