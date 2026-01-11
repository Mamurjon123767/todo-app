from django.urls import path
from.views import todo_list, completed_todos, pending_todos
urlpatterns = [
    path('todos/', todo_list),
    path('tods/completed',completed_todos, name="completed todos"),
    path('todos/pending/',pending_todos, name="pending todos"),
]