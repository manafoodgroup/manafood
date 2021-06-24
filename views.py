from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def mainpage(request):
    return render(request,"mainrestaurant/index.html")

def ordercard(request):
    return render(request,"mainrestaurant/cardslider.html")