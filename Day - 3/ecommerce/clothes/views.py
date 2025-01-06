from django.shortcuts import render
from django.http import HttpResponse
from .models import Clothes

# Create your views here.
def home(request):
    clothes = Clothes.objects.all()
    return render(request, 'clothes-list.html', {"clothes" : clothes})
def categories(request):
    return HttpResponse("Clothes Categories Page")
