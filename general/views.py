from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import UserForm




def title(request):
    userform = UserForm()
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            return HttpResponseRedirect(request.path)
    return render(request, 'index.html', {"form": userform})

def news(request):
    return render(request, 'news.html')

def documents(request):
    return render(request, 'documents.html')