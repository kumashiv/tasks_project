from django.contrib import admin

# Register your models here.
from .models import Thing, Task

admin.site.register(Thing)
admin.site.register(Task)