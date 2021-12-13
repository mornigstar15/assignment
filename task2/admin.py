from django.contrib import admin
from .models import task2

class task2Admin(admin.ModelAdmin):
    model = task2
    list_display = ['si_no', 'title']

admin.site.register(task2, task2Admin)
