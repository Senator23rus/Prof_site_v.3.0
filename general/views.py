from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.core.paginator import Paginator
# from .forms import UserForm
from .models import Appeal, ShortNewsOnMainPage, News




def title(request):
    appeal = Appeal.appeal.all()
    short_news = ShortNewsOnMainPage.sh_news.all()
    return render(request, 'index.html', {"appeal": appeal, "short_news": short_news})

def create(request):
    if request.method == "POST":
        appeal = Appeal()
        # if appeal.is_valid():
        appeal.name = request.POST.get("name")
        appeal.e_mail = request.POST.get("e_mail")
        appeal.filial = request.POST.get("filial")
        appeal.message = request.POST.get("message")
        appeal.save()
    return HttpResponseRedirect("/")

def news(request, page=1):
    news = News.objects.all()
    paginator = Paginator(news, 5)
    return render(request, 'news.html', {'news': paginator.page(page)})

def documents(request):
    return render(request, 'documents.html')