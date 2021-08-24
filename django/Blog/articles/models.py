from django.db import models

# Create your models here.


class articles(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    body = models.TextField()
    date = models.TimeField(auto_now=True)
    image = models.ImageField(default='default.jpg', blank=True)
    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + ' ...'
