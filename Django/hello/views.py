from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def victor(request):
    return HttpResponse("Hello, Victor!")

# def users(request, name):
#     return HttpResponse(f"Hello, {name.capitalize()}!")
def users(request, name):
    return render(request, "hello/users.html", {
        "name":name.capitalize()
    })