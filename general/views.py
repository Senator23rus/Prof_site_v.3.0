from urllib import request

from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.core.paginator import Paginator
# from .forms import UserForm
from .models import Appeal, AppealForm, ShortNewsOnMainPage, News, Document, Сhairman
from django.contrib import messages



def title(request):
    appeal = Appeal.appeal.all()
    short_news = ShortNewsOnMainPage.sh_news.all()
    return render(request, 'index.html', {"appeal": appeal, "short_news": short_news})


def create(request):

    if request.method == "POST":
        appeal = AppealForm(request.POST)
        if appeal.is_valid():
        # appeal.name = request.POST.get("name")
        # appeal.e_mail = request.POST.get("e_mail")
        # appeal.filial = request.POST.get("filial")
        # appeal.message = request.POST.get("message")
            appeal.save()
        else:
            messages.error(request, 'Заполните правильно форму')
            return HttpResponseRedirect("/#contact_us")

    messages.info(request, 'Спасибо, Ваше обращение принято!')
    return HttpResponseRedirect("/#contact_us")


def filials(request):
    filial = Сhairman.chairman_object.all()
    return render(request, 'filials.html', {"filial": filial})


def documents(request):
    docs = Document.doc_object.all()
    return render(request, 'documents.html', {"docs": docs})



def news(request, page=1):
    news_block = News.news_object.all()
    paginator = Paginator(news_block, 5)
    return render(request, 'news.html', {'news_block': paginator.page(page)})
