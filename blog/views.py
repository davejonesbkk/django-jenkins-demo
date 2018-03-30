from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse('Hello world')

def homepage(request):
	return HttpResponse('This is the homepage')


# Create your views here.
