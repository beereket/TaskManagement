from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .models import Todo

# List all todos
def index(request):
    todos = Todo.objects.all()
    return render(request, "base.html", {"todo_list": todos})

# Add a new todo
@require_http_methods(["POST"])
def add(request):
    title = request.POST["title"]
    todo = Todo(title=title)
    todo.save()
    return redirect("index")

# Toggle completion status
def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.complete = not todo.complete
    todo.save()
    return redirect("index")

# Delete a todo
def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect("index")
