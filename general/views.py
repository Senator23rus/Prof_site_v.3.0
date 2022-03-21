from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotFound
from django.shortcuts import render
# from .forms import UserForm
from .models import Appeal




def title(request):
    appeal = Appeal.appeal.all()
    return render(request, 'index.html', {"appeal": appeal})

def create(request):
    if request.method == "POST":
        appeal = Appeal(request.POST)
        if appeal.is_valid():
            appeal.name = request.POST.get("name")
            appeal.e_mail = request.POST.get("e_mail")
            appeal.filial = request.POST.get("filial")
            appeal.message = request.POST.get("message")
            appeal.save()
    return HttpResponseRedirect("/")

def news(request):
    return render(request, 'news.html')

def documents(request):
    return render(request, 'documents.html')