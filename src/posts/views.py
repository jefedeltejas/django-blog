from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create them views here.
from .models import Post

def post_create(request):
    return HttpResponse("<h1>Wuppud make a new post!!!!</h1>")

def post_detail(request):
    context = {
        "title": "Detail"
    }
    return render(request, "index.html", context)

def post_list(request):
    queryset = Post.objects.all()
    context = {
        "object_list": queryset,
        "title": "Yo mama"
    }
    return render(request, "index.html", context)
    #return HttpResponse("<h1>Zie master list!!!!</h1>")

def post_update(request):
    return HttpResponse("<h1>Update!!!!</h1>")

def post_delete(request):
    return HttpResponse("<h1>Delete!!!!</h1>")
