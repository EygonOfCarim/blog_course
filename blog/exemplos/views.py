from django.shortcuts import render


def exemplos(request):
    return render(request, 'exemplos/home.html')
