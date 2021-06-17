from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist_app.models import Tasklist
from todolist_app.form import TaskForm

def todolist(request):
    all_tasks = Tasklist.objects.all()
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        Tasklist.save()
        return redirect('todolist.html')
    else:
        all_tasks = Tasklist.objects.all()
        return render(request, 'todolist.html',{'all_tasks':all_tasks})

def contact(request):
    context = {
        'welcome_contact': "Hey, Welcome to contact page",
    }
    return render(request,'contact.html',context)

def about(request):
    context = {
        'welcome_about': "Hey, Welcome to about page",
    }
    return render(request, 'about.html', context)
