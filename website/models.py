from django.db import models

# Create your models here.

class FeedBack(models.Model):

    name = models.CharField(max_length=250)
    email = models.CharField(max_length=300)
    subject = models.CharField(max_length=400)
    message = models.TextField(max_length=10000)