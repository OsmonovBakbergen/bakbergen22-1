from django.http import HttpResponse
from django.shortcuts import render
import datetime


# Create your views here.


def hello(request):
    if request.method == 'GET':
        return HttpResponse('Hello! Its my project')


def now_date(request):
    if request.method == 'GET':
        return HttpResponse(f'{datetime.datetime.now()}')


def goodbye(request):
    if request.method == 'GET':
        return HttpResponse('Goodbye user!')