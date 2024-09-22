from django.shortcuts import render,get_object_or_404, redirect
from .models import Purchased


def purchased(request):
    current_user = request.user
    purchaseds = Purchased.objects.filter(author=current_user)
    return render(request, 'purchased/purchased.html', {'purchaseds': purchaseds})


def delete_purchased(request, purchased_id):
    purchased = get_object_or_404(Purchased, pk=purchased_id, author=request.user)
    if request.method == 'POST':
        purchased.delete()
        return redirect('purchased')
    return redirect('purchased')