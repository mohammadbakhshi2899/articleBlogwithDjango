from django.shortcuts import render, HttpResponse


def about(request):
    # return HttpResponse("Hi I am mohammad bakhshi who is the best programmer in this world")
    return render(request, 'about.html')

def home(request):
    # return HttpResponse('home')
    return render(request, 'home.html')
# /home/mohammad/PycharmProjects/pythonProject/Django/Blog/django/Blog/templates/home.html

