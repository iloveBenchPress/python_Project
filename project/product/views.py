from django.shortcuts import render,get_object_or_404, redirect
from .models import Product
from Purchased.models import Purchased
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


def index(request):
    products = Product.objects.all()
    return render(request,'products/index.html',{'products':products})


def main(request):
    return render(request, 'products/main.html', {'main': main})

@login_required(login_url="loginuser")
def detail(request,product_id):
    product = get_object_or_404(Product,pk=product_id)
    return render(request,'products/details.html',{'product': product})

def deleteprod(request, product_id):
    product = get_object_or_404(Product,pk=product_id)
    if request.method == "POST":
        del_obj=Purchased(title=product.title,description=product.description,price=product.price)

        del_obj.save()
        product.delete()
        return redirect('index')
    return redirect('index')


def signupuser(request):
    if request.method == "GET":
        return render(request, 'products/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'products/signupuser.html',
                              {'form': UserCreationForm(),
                               'error': 'Такое имя пользователя уже существует. Задайте другое'})
        else:
            return render(request, 'products/signupuser.html', {'form': UserCreationForm(), 'error': 'Пароли не совпадают'})

def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('index')


def loginuser(request):
    if request.method == "GET":
        return render(request,'products/loginuser.html',{'form': AuthenticationForm()})
    else:
        user = authenticate(request,username=request.POST['username'],password= request.POST['password'])
        if user is None:
            return render(request, 'products/loginuser.html',
                          {'form': AuthenticationForm(),
                           'error': 'Неверные данные для входа'})
        else:
            login(request, user)
            return redirect('index')