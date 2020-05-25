from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная'
    }
    return render(request, 'home/index.html', context=data)