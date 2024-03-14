from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def monday(request):
    return HttpResponse('<h4> Monday is hard day')


def tuesday(request):
    return HttpResponse('<h4> Tuesday is not easy</h4>')
