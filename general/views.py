from django.shortcuts import render




def title(request):
    return render(request, 'index.html')
