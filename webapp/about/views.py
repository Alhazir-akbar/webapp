from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'nama': 'hello world',
    }
    return render(request, 'index.html', context)