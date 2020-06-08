import datetime

from django.shortcuts import render


def home(request):
    date = datetime.datetime.now().date()
    name = 'Evgen'
    result = { 'date': date, 'name': name}
    return render(request, 'home.html', result)