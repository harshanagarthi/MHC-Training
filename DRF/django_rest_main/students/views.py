from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def students(request):
    students =[
        {
            'id': 160,
            'name': 'Harsha',
            'age': 22
        }
        ]
    
    return HttpResponse(students)