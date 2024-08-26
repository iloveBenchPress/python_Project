from django.shortcuts import render
from .models import Skills

def index(request):
    projects = Skills.objects.all()
    return render(request,'skills/index.html',{'projects':projects})

def main(request):
    return render(request, 'blog/main.html', {'main': main})