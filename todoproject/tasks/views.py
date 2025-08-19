from django.shortcuts import render, redirect
from tasks.models import Task
from django.contrib.auth.decorators import login_required
from tasks.forms import TaskForm
from django.http import JsonResponse
from django.utils import timezone
from datetime import date

@login_required
def kanban_board(request):
    tasks = Task.objects.filter(user=request.user)
    pending = []
    done = []

    for task in tasks:
        # محاسبه روزهای باقی‌مانده
        if task.due_date:
            task.days_left = (task.due_date - date.today()).days
        else:
            task.days_left = None

        if task.completed:
            done.append(task)
        else:
            pending.append(task)

    return render(request, "tasks/kanban.html", {
        'pending': pending,
        'done': done,
    })

@login_required
def update_task_status(request):
    if request.method == "POST":
        task_id = request.POST.get("task_id")
        status = request.POST.get("status")  # 'pending' یا 'done'
        task = Task.objects.get(id=task_id, user=request.user)
        task.completed = True if status == "done" else False
        task.save()
        return JsonResponse({"success": True})
    return JsonResponse({"success": False})



@login_required
def task_list(request):
    sort = request.GET.get('sort', 'due_date')  
    direction = request.GET.get('dir', 'asc')  
    order = sort if direction == 'asc' else f"-{sort}"
    tasks = Task.objects.filter(user=request.user).order_by(order)

    # محاسبه روز باقی‌مانده
    for task in tasks:
        if task.due_date:
            delta = task.due_date - timezone.now().date()
            task.days_left = delta.days
        else:
            task.days_left = None

    return render(request, "tasks/task_list.html", {"tasks": tasks, "sort": sort, "dir": direction})

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
