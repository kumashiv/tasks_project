
from django.http import HttpResponse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from todo.models import Thing, Task


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





class ThingCreate(CreateView):
    model = Thing
    fields = '__all__'
    success_url = reverse_lazy('todo:all')


class ThingUpdate(UpdateView):
    model = Thing
    fields = '__all__'
    success_url = reverse_lazy('todo:all')


class ThingDelete(DeleteView):
    model = Thing
    fields = '__all__'
    success_url = reverse_lazy('todo:all')





class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('todo:all')


class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('todo:all')


class TaskDelete(DeleteView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('todo:all')
