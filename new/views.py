from django.shortcuts import render,redirect
from .models import Todo
# Create your views here.
from django.views.decorators.http import require_POST
from .forms import TodoForm

def home(request):
    todo_list=Todo.objects.order_by('id')
    form=TodoForm()
    context={
        'todo_list':todo_list, 
        'form':form

    }
    return render(request, 'todo/home.html',context)


@require_POST

def addTodo(request):
    form=TodoForm(request.POST)

    if form.is_valid():
        new_todo=Todo(text=request.POST['text'])
        new_todo.save()
    # print(request.POST['text'])
    return redirect('home')


def completeTodo(request, todo_id):
    todo=Todo.objects.get(pk=todo_id)
    todo.complete=True
    todo.save()

    return redirect('home')

def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('home')

def deleteAdd(request):
    Todo.objects.all().delete()
    return redirect('home')