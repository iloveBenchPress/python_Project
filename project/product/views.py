from django.shortcuts import render,get_object_or_404, redirect
from .models import Product,CustomUser
from Purchased.models import Purchased
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .utils import search_products
from .forms import WalletForm
from django.contrib import messages

def index(request):
    if request.user.is_authenticated:
        product, search_query = search_products(request)
        wallet_user = get_object_or_404(CustomUser, user=request.user)
        return render(request, 'products/index.html',
                      {'products': product, 'search_query': search_query, 'wallet_user': wallet_user})
    else:
        product, search_query = search_products(request)
        return render(request, 'products/index.html',
                      {'products': product, 'search_query': search_query})


def main(request):
    return render(request, 'products/main.html', {'main': main})

@login_required(login_url="loginuser")
def detail(request,product_id):
    wallet_user = CustomUser.objects.get(user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/details.html', {'product': product, 'wallet_user': wallet_user})

def deleteprod(request, product_id):
    product = get_object_or_404(Product,pk=product_id)
    wallet_user = CustomUser.objects.get(user=request.user)
    product.price = int(product.price)
    if wallet_user.value >= product.price:
        if request.method == "POST":
            wallet_user.value -= product.price
            wallet_user.save()
            del_obj=Purchased(title=product.title,description=product.description,price=product.price,image=product.image.path,author=request.user)
            del_obj.save()
            product.delete()
            return redirect('index')
        return redirect('index')
    else:
        return render(request, 'products/details.html', {
                 'product': product,
                 'wallet_user': wallet_user,
                 'error_message': 'У вас недостаточно средств.'
             })



def signupuser(request):
    if request.method == "GET":
        return render(request, 'products/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                # Создаем CustomUser после создания User
                custom_user = CustomUser.objects.create(user=user)
                custom_user.save()
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


def edit_wallet(request):
    profile = request.user.customuser
    if request.method == "POST" and request.user.is_authenticated:
        form = WalletForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = WalletForm(instance=profile)

    context = {'form': form}
    return render(request, 'products/edit_wallet.html', context)


