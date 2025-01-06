from django.shortcuts import render
from django.http import HttpResponse
from .models import Electronics

# Create your views here.
def home(request):
    electronics = Electronics.objects.all()
    return render(request, 'electronic-list.html', {'electronics': electronics})
def categories(request):
    return HttpResponse("Electronics Categories Page")