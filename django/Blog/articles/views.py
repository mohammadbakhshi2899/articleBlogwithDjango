from django.shortcuts import render, HttpResponse, redirect
from . import models
from django.contrib.auth.decorators import login_required
from . import forms as ourForms
# Create your views here.


def articles_list(request):
    articles = models.articles.objects.all().order_by('date')
    listArticles = {'listArticles':articles}
    return render(request, "articles/articles.html", listArticles)


def articles_details(request, slug):
    # return HttpResponse(slug)
    article = models.articles.objects.get(slug=slug)
    return render(request, 'articles/details.html', {'article':article})

@login_required(login_url='/accounts/login')
def publish_article(request):
    if request.method == "POST":
        form = ourForms.registerArticle(request.POST,request.FILES)
        if form.is_valid :
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect("articles:list")

    form = ourForms.registerArticle()
    return render(request, 'articles/publish_article.html', {'form':form})