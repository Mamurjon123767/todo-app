from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import TodoForm

from .models import Todo

def todo_list(request):
    todos = Todo.objects.all()
   
    return render(request, 'todoapp/todo_list.html', {'todos': todos})


def pending_todos(request):
    todos = Todo.objects.filter(is_completed = False)
    return render(request, 'todoapp/pending_todos.html', {'todos': todos})

    

def completed_todos(request):
    todos = Todo.objects.filter(is_completed = False)
    return render(request, 'todoapp/completed_todos.html', {'todos': todos})


def completed_todos(request):
    todos = Todo.objects.filter(is_completed = True)
    response = ""

    for todo in todos:
        response +=f"{todo.title}/n"

    return HttpResponse(response)


def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()

    return render(request, 'todoapp/todo_form.html',{'form': form})

def update_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)


    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)

    return render(request, 'todoapp/todo_form.html',{'form': form})
    
def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)

    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')

    return render(request, 'todoapp/todo_delete.html',{'todo': todo})