from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
from django.db.models import Q
from tasks.forms import TaskForm, SearchForm
from tasks.forms import TaskForm
from tasks.models import Task


def test_view(request):
    return HttpResponse(f"test4month! {random.randint(1,100)}")


def home_page_view(request):
    if request.method == "GET":
        return render(request, "base.html")



def task_list_view(request):
    tasks = Task.objects.all()
    if request.method == "GET":
        search = request.GET.get("search")
        category = request.GET.get("category")
        ordering = request.GET.get("ordering")
        form = request.GET.get("form")
        if search:
            tasks = tasks.filter(Q(title__icontains=search) | Q(description__icontains=search))
        if category:
            tasks = tasks.filter(category=int(category))
        if ordering:
            tasks = tasks.order_by(ordering)

        return render(request,"tasks/task_list.html",{"tasks":tasks,"form":form})



def task_detail_view(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request,"tasks/task_detail.html",{"task":task})



def task_create_view(request):
    if request.method == "GET":
        form = TaskForm()
        return render(request,"tasks/task_create.html",{"form":form})
    if request.method == "POST":
        form = TaskForm(request.POST)
        if not form.is_valid():
            return render(request,"tasks/task_create.html",{"form":form})
        elif form.is_valid():
            form.save()
        return redirect("task-list")