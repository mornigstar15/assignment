from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import Assingment
from .forms import UserCreationForm, TaskCreationForm

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class TasksView(CreateView):
    form_class = TaskCreationForm
    success_url = reverse_lazy('tasks')
    template_name = 'tasks/create.html'

class TasksListView(generic.ListView):
    model = Assingment
    template_name = 'tasks/list.html'
    paginate_by = 5
