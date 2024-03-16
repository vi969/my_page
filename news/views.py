from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def get_news(request):
    context = {
        'power_man': 'Narve Laeret',
        'bar_name': 'Bob’s BBQ & Grill',
        'count_needle': 1790,
    }
    return render(request, 'news/guinnessworldrecords.html', context=context)
