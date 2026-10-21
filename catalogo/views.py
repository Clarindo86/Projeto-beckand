from django.shortcuts import render

from django.http import HttpResponse

def home(req):
        return HttpResponse('welcome!')

def login(req):
        return HttpResponse('Batata')

def sobre(req):
        return HttpResponse('Ivison Raparigueiro!')


