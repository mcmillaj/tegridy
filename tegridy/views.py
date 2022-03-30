from django.http import HttpResponse
from django.shortcuts import render

def home(request):
   return render(request, 'tegridy/home.html', {})

def reviews(request):
    return render(request, 'tegridy/reviews.html', {})

def about(request):
    return render(request, 'tegridy/about.html', {})