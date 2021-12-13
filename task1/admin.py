from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserChangeForm, TaskCreationForm
from .models import User, Assingment

class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ['username',]

class TaskAdmin(admin.ModelAdmin):
    add_form = TaskCreationForm
    model = Assingment
    list_display = ['task_title', 'task_description']

admin.site.register(User, UserAdmin)

admin.site.register(Assingment, TaskAdmin)
