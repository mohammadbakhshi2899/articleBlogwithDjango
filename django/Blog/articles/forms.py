from django import forms as realForms
from .models import articles
class registerArticle(realForms.ModelForm):
    class Meta :
        model = articles
        fields = ['title', 'slug', 'body', 'image']