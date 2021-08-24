from django.shortcuts import render, HttpResponse
from . import models
# Create your views here.


def articles_list(request):
    articles = models.articles.objects.all().order_by('date')
    listArticles = {'listArticles':articles}
    return render(request, "articles/articles.html", listArticles)


def articles_details(request, slug):
    # return HttpResponse(slug)
    article = models.articles.objects.get(slug=slug)
    return render(request, 'articles/details.html', {'article':article})