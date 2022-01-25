from django.shortcuts import render

from django.urls import path, include
def index(request):
    return render(request, 'club\index.html')

