from django.shortcuts import render,get_object_or_404, redirect
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required



@login_required(login_url="loginuser")
def reviews(request):
    reviews = Review.objects.order_by('-created')
    if request.method == 'GET':

        return render(request, 'review/reviews.html',{'reviews':reviews,'form':ReviewForm(user=request.user),'author': request.user})
    else:
        try:
            form = ReviewForm(request.POST or None, user=request.user)
            new_review = form.save(commit=False)
            new_review.user = request.user
            new_review.save()
            return redirect('reviews')
        except ValueError:
            return render(request, 'review/reviews.html',
                          {'reviews':reviews,'form': ReviewForm(user=request.user), 'error': 'Переданы неверные данные. Попробуйте ещё раз'})




