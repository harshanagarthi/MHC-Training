from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Groceries Page")
def categories(request):
    return HttpResponse("Groceries Categories Page")