from django.shortcuts import render
from django.http import HttpResponse

from .models import Task

def taskList(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/list.html', {'tasks': tasks})


def helloWorld(request):
    return HttpResponse('Aqui pode ser retornado uma reposta http, como também um template html com todas suas informações.')


def yourName(request, name):
    return render(request, 'tasks/yourname.html', {'name': name})  
    