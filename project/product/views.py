from django.shortcuts import render
from .models import Product

def index(request):
    projects = Product.objects.all()
    return render(request,'products/index.html',{'projects':projects})

def main(request):
    return render(request, 'products/main.html', {'main': main})