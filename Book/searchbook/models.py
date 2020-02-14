from django.db import models

# Create your models here.

class Data(models.Model):
    name = models.TextField()
    title = models.TextField()
    author = models.TextField()
    
class DB(models.Model):
    time = models.TextField()
    kind = models.TextField()
    date = models.TextField()
    title = models.TextField()
    author = models.TextField()
    genre = models.TextField()