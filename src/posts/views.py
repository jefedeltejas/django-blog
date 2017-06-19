from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def post_create(request):
    return HttpResponse("<h1>Wuppud make a new post!!!!</h1>")

def post_detail(request):
    return HttpResponse("<h1>A post in all its glory!!!!</h1>")

def post_list(request):
    return HttpResponse("<h1>Zie master list!!!!</h1>")

def post_update(request):
    return HttpResponse("<h1>UPdate!!!!</h1>")

def post_delete(request):
    return HttpResponse("<h1>Delete!!!!</h1>")
