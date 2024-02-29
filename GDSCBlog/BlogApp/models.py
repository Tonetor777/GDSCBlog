from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Post (models.Model):
    title = models.CharField(max_length = 255 , unique = True)
    content = models.TextField()
    catagory = models.CharField(max_length = 255)
    image = models.ImageField()
    tags = ArrayField(models.CharField(max_length = 255))

    def __str__(self):
        return self.title