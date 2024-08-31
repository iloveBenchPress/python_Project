from django.shortcuts import render,get_object_or_404, redirect
from .models import Product

def index(request):
    products = Product.objects.all()
    return render(request,'products/index.html',{'products':products})

def main(request):
    return render(request, 'products/main.html', {'main': main})

def detail(request,product_id):
    product = get_object_or_404(Product,pk=product_id)
    return render(request,'products/details.html',{'product': product})

def deleteprod(request, product_id):
    product = get_object_or_404(Product,pk=product_id)
    if request.method == "POST":
        product.delete()
        return redirect('index')
    return redirect('index')