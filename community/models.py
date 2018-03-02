# community/models
from django.db import models

# Create your models here.
# 게시물 관련 클래스

class Article(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    contents = models.TextField()
    url = models.URLField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)