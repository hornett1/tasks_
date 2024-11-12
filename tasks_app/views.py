from typing import Any
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import *
from .models import *
from .forms import *
import json

# Create your views here.



class DetailTask(DetailView):
    model = Task
    template_name = 'tasks_app/task_detail.html'
    context_object_name = 'task'

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        form.instance.author = request.user
        form.instance.task = self.get_object()
        print(request.POST)

        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return redirect("/")
        
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.all()
        context["form"] = CommentForm()
        return context
    

class TaskListViewProfile(TemplateView):
    template_name = 'tasks_app/task_by_status.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['not_started_tasks'] = Task.objects.filter(status='not_started', task_author=self.request.user)
        context['in_progress_tasks'] = Task.objects.filter(status='in_progress', task_author=self.request.user)
        context['completed_tasks'] = Task.objects.filter(status='completed', task_author=self.request.user)

        return context


class main(TemplateView):
    template_name = 'tasks_app/main.html'


def update_task_status(request, task_id):
    if request.method == "POST":
       
        task = Task.objects.get(id=task_id)

        
        new_status = request.POST.get('status')

        
        if new_status in dict(Task.STATUS_CHOICES).keys():
            task.status = new_status
            task.save()  

        return redirect('task-status')  
    

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('main')  
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = RegisterForm()
    return render(request, 'tasks_app/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('main')  
        else:
            messages.error(request, 'Неверное имя пользователя или пароль')
    
    return render(request, 'tasks_app/login.html')

class AddTaskView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm  
    template_name = 'tasks_app/add_task.html'  
    success_url = '/task/profile'  
    def form_valid(self, form):
        form.instance.task_author = self.request.user
        print(form.instance.task_author)
        return super().form_valid(form)

class DeleteTaskView(DeleteView):
    model = Task
    success_url = '/task/profile'  

    def get_object(self, queryset=None):
        return Task.objects.get(pk=self.kwargs['pk'])

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)





