from django.urls import path
from.views import todo_list, completed_todos, pending_todos, add_todo, update_todo, delete_todo
urlpatterns = [
    path('todos/', todo_list, name="todo_list"),
    path('todos/completed/',completed_todos, name="completed_todos"),
    path('todos/pending/',pending_todos, name="pending_todos"),
    path('todos/add/', add_todo, name = 'add_todo'),
    path('todos/update/<int:pk>/', update_todo, name= "update_todo"),
    path('todos/delete/<int:pk>/', delete_todo, name = "delete_todo"),
]