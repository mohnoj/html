from django.shortcuts import render
from django.views.generic import ListView
from . import models

# Create your views here.
class HomePageView(ListView):
	mode1 = models.Post
	template_name = 'blog/blog_post.html'