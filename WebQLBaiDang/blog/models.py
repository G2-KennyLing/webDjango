from django.db import models
from django.conf import settings
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=1000)
    body = models.TextField()
    createAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)