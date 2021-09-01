from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class articles(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    body = models.TextField()
    date = models.TimeField(auto_now=True)
    image = models.ImageField(default='default.jpg', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + ' ...'
