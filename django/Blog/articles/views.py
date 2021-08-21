from django.shortcuts import render
from . import models
# Create your views here.


def articles_list(request):
    articles = models.articles.objects.all().order_by('date')
    listArticles = {'listArticles':articles}
    return render(request, "articles/articles.html", listArticles)
