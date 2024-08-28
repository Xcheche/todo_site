from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "todos/index.html")


def create_todos(request):
    return render(request, "todos/create_todos.html")
