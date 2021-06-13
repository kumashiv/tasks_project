
from django.urls import path

from . import views

app_name = 'todo'

urlpatterns = [
    # path('', views.index, name='index'),

    path('', views.MainView.as_view(), name='all'),
    path('task/', views.TaskView.as_view(), name='task_list'),

]

