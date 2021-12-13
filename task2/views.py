from django.shortcuts import render
from .models import task2
from django.views import generic

# Create your views here.
class Task2View(generic.ListView):
    template_name = 'task2.html'

    def get_queryset(self):
        return task2.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Task2View, self).get_context_data(**kwargs)
        context['main'] = self.get_queryset().filter(parent_id__isnull=True)
        context['sub'] = self.get_queryset().filter(parent_id__in=context['main'])
        context['sub_sub'] = self.get_queryset().filter(parent_id__in=context['sub'])
        return context
