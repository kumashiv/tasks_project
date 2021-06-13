from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")



from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from todo.models import Thing, Task
#from autos.forms import MakeForm

# Create your views here.


class MainView(View):
    def get(self, request):
        thing_list = Thing.objects.all()
        task_count = Task.objects.all().count()


        ctx = {'thing_list': thing_list, 'task_count': task_count}
        return render(request, 'todo/thing_list.html', ctx)


class TaskView(View):
    def get(self, request):
        task_list = Task.objects.all()
        ctx = {'task_list': task_list}
        return render(request, 'todo/task_list.html', ctx)

