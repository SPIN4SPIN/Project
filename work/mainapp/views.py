from django.shortcuts import render
from datetime import datetime


def index(request):
    now = datetime.now()
    sec = now.year
    number = [sec + 100, sec + 200, sec + 300, sec + 400, sec + 100, sec + 200, sec + 300, sec + 400]
    context = {
        'date_time': now.strftime('%d-%m-%Y %H:%M:%S'),
        'number': number,
    }
    return render(request, 'mainapp/index.html', context)
