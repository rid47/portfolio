from django.db import models

# Create your models here.

# Creating child class Job from parent class Model of models module


class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)


