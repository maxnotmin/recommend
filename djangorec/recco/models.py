from django.db import models

# Create your models here.

class Show(models.Model):
    title = models.TextField()
    description = models.TextField()
    tags = models.TextField()
    summary = models.TextField(default="Summary Default")