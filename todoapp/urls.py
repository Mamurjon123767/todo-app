from django.urls import path
from.views import todo_list, completed_todos, pending_todos, add_todo, update_todo, delete_todo
urlpatterns = [
    path('todos/', todo_list, name="todo_list"),
    path('tods/completed',completed_todos, name="completed todos"),
    path('todos/pending/',pending_todos, name="pending todos"),
    path('todos/add/', add_todo, name = 'add_todo'),
    path('todos/update/<int:pk>/', update_todo, name= "update_todo"),
    path('todos/delete/<int:pk>/', delete_todo, name = "delete_todo"),
]