from django.shortcuts import render,get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm


def todos(request):
    todos = Todo.objects.order_by('-date_completed')
    if request.method == 'GET':
        return render(request, 'blog/todos.html',{'todos':todos,'form':TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            new_todo = form.save(commit=False)
            new_todo.user = request.user
            new_todo.save()
            return redirect('todos')
        except ValueError:
            return render(request, 'blog/todos.html',
                          {'todos':todos,'form': TodoForm(), 'error': 'Переданы неверные данные. Попробуйте ещё раз'})

# def detail(request,blog_id):
#     blog = get_object_or_404(Blog,pk=blog_id)
#     return render(request,'blog/details.html',{'blog':blog})


