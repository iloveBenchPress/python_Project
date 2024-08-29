from django.shortcuts import render,get_object_or_404, redirect
from .models import Review
from .forms import TodoForm


def reviews(request):
    reviews = Review.objects.order_by('-created')
    if request.method == 'GET':
        return render(request, 'review/reviews.html',{'reviews':reviews,'form':TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            new_todo = form.save(commit=False)
            new_todo.user = request.user
            new_todo.save()
            return redirect('reviews')
        except ValueError:
            return render(request, 'reviews/reviews.html',
                          {'reviews':reviews,'form': TodoForm(), 'error': 'Переданы неверные данные. Попробуйте ещё раз'})

# def detail(request,blog_id):
#     reviews = get_object_or_404(Blog,pk=blog_id)
#     return render(request,'reviews/details.html',{'reviews':reviews})


