from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo

def todo_list(request):
    todos = Todo.objects.all()
    response = ""

    for todo in todos:
        status = "Done" if todo.is_completed else "Not done"
        response += f"{todo.title} - {status}/n"


    return HttpResponse(response)



def pending_todos(request):
    todos = Todo.objects.filter(is_completed = False)
    response = ""

    for todo in todos:
        response +=f"{todo.title}/n{todo.priority}/n{todo.due_date}/n"

    return HttpResponse(response)




def completed_todos(request):
    todos = Todo.objects.filter(is_completed = True)
    response = ""

    for todo in todos:
        response +=f"{todo.title}/n"

    return HttpResponse(response)


