from django.urls import path
from.views import todo_list, completed_todos, pending_todos, add_todo
urlpatterns = [
    path('todos/', todo_list, name="todo_list"),
    path('tods/completed',completed_todos, name="completed todos"),
    path('todos/pending/',pending_todos, name="pending todos"),
    path('todos/add/', add_todo, name = 'add_todo'),
]