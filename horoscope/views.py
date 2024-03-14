from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def leo(request):
    return HttpResponse('<h3>Sign of zodiac "Leo"</h3>')