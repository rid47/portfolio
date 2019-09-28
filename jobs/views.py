from django.shortcuts import render
from .models import *

# Create your views here.


def home(request):

    jobs = Job.objects.all
    template = 'jobs/home.html'
    context ={
        'jobs': jobs,
    }
    return render(request, template, context)
