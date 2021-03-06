from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print("the form is going to be checked ")
        if form.is_valid():
            # login
            user = form.save()
            login(request, user)
            if 'next' in request.POST :
                return redirect(request.POST.get('next'))
            return redirect("articles:list")
        else:
            return HttpResponse("probably you did not fill the form accurate")

    form = UserCreationForm()
    return render(request, "accounts/signup.html", {'form':form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #login user
            user = form.get_user()
            login(request, user)
            return redirect("articles:list")
        else:
            return HttpResponse("probably you did not fill the form accurate")
    else:
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form':form})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('articles:list')
    else:
        return HttpResponse("you are not logged in")
