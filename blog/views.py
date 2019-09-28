from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.


def allblogs(request):

    blogs = Blog.objects.all
    template = 'blogs/allblogs.html'
    context ={
        'blogs': blogs,
    }
    return render(request, template, context)


def detail(request,blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    context ={
        'blog': detailblog,
    }
    template = 'blogs/detail.html'

    return render(request, template,context)