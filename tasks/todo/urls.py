
from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    # path('', views.index, name='index'),

    path('', views.MainView.as_view(), name='all'),
    path('thing/create/', views.ThingCreate.as_view(), name='thing_create'),
    path('thing/<int:pk>/update/', views.ThingUpdate.as_view(), name='thing_update'),
    path('thing/<int:pk>/delete/', views.ThingDelete.as_view(), name='thing_delete'),

    path('task/', views.TaskView.as_view(), name='task_list'),
    path('task/create/', views.TaskCreate.as_view(), name='task_create'),
    path('task/<int:pk>/update/', views.TaskUpdate.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', views.TaskDelete.as_view(), name='task_delete'),

]

