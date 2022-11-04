from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article')
    title = models.CharField(max_length=150)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    body = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comment')
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
