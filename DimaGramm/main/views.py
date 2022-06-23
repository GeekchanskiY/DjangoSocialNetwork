from django.shortcuts import render, HttpResponse
from .forms import *
# Create your views here.


def index(request):
    return HttpResponse("Hi on DimaGramm")


def user_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("User created successfully")
        else:
            return HttpResponse("Something went wrong")
    else:
        return render(request, 'index.html', {"form": CustomUserCreationForm})
