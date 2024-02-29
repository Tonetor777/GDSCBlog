from django.db import models
from BlogApp.models import Post
# Create your models here.

class Comment (models.Model):
    content = models.TextField()
    author = models.CharField(max_length = 255)
    publishedDate = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post , on_delete = models.CASCADE)

