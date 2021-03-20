from django.shortcuts import render
from datetime import datetime

import csv


def index(request):
    with open('mainapp/excel/guns.csv') as guns_file:
        reader = csv.DictReader(guns_file, delimiter=";")
        sum_year = 0
        sum_pop = 0
        for row in reader:
            sum_year += int(row['year'])
            sum_pop += float(row['pop'].replace(',', '.'))

    now = datetime.now()
    sec = now.year
    number = [sec + 100, sec + 200, sec + 300, sec + 400]

    context = {
        'date_time': now.strftime('%d-%m-%Y %H:%M:%S'),
        'number': number,
        'sum_year': sum_year,
        'sum_pop': f'{sum_pop:.4f}',
    }
    return render(request, 'mainapp/index.html', context)
