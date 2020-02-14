from django.db import models

# Create your models here.

class Data(models.Model):
    name = models.TextField()
    title = models.TextField()
    author = models.TextField()
    
