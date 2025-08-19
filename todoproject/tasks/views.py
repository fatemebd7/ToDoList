from django.shortcuts import render, redirect
from tasks.models import Task
from django.contrib.auth.decorators import login_required
from django import forms

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "due_date", "priority", "category"]

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by("completed", "due_date")
    return render(request, "tasks/task_list.html", {"tasks": tasks})

@login_required
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("task_list")
    else:
        form = TaskForm()
    return render(request, "tasks/task_form.html", {"form": form})

@login_required
def task_toggle(request, pk):
    task = Task.objects.get(id=pk, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect("task_list")

@login_required
def task_delete(request, pk):
    task = Task.objects.get(id=pk, user=request.user)
    task.delete()
    return redirect("task_list")

@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)
    total = tasks.count()
    done = tasks.filter(completed=True).count()
    pending = tasks.filter(completed=False).count()
    return render(request, "tasks/dashboard.html", {
        "total": total,
        "done": done,
        "pending": pending,
    })
