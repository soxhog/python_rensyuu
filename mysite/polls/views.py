from django.shortcuts import render
from django.http import HttpResponse
def index(request):
	return HttpResponse("Hello, World. Your're at the polls index.")
