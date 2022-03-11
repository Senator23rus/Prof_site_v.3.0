from django.shortcuts import render




def title(request):
    return render(request, 'index.html')


def news(request):
    return render(request, 'news.html')