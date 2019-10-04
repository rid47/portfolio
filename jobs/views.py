from django.shortcuts import render
from .models import *

# Create your views here.


def home(request):

    jobs = Job.objects.all()
    for job in jobs:
        print(job.image.url)
    template = 'jobs/home.html'
    context ={
        'jobs': jobs,
    }
    return render(request, template, context)
