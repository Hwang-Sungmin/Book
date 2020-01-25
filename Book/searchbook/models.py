from django.db import models

# Create your models here.

class Data(models.Model):
    title = models.TextField()
    author = models.TextField()