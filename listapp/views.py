from .forms import AddTaskForm, RegisterUserForm, UpdateTaskForm

from .models import *

from .utils import DataMixin

from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView

from django.shortcuts import HttpResponse, redirect, render

from django.urls import reverse_lazy

from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView


def logout_view(request):
    logout(request)
    return redirect('about')


class TaskView(DataMixin, DeleteView):
    model = Task
    fields = ('title', 'description', 'is_complete', 'time_created', )
    template_name = 'listapp/task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_custom_context(title=f'{self.request.user}`s Task')
        return dict(list(context.items()) + list(data.items()))


class AboutView(DataMixin, TemplateView):
    template_name = 'listapp/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_custom_context(title='About Page')
        return dict(list(context.items()) + list(data.items()))


class TdlView(DataMixin, TemplateView):
    template_name = 'listapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_custom_context(title='TDL Page')
        return dict(list(context.items()) + list(data.items()))


class UpdateTaskView(UpdateView):
    model = Task
    form_class = UpdateTaskForm
    template_name = 'listapp/update_task.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Page'
        return context


class DeleteTaskView(DeleteView):
    model = Task
    success_url = reverse_lazy('index')
    template_name = 'listapp/delete_task.html'


class UserTasksListView(DataMixin, ListView):
    model = Task
    paginate_by = 3
    template_name = 'listapp/index.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_custom_context(title='Tasks List')
        return dict(list(context.items()) + list(data.items()))

    def get_queryset(self):
        return Task.objects.filter(
            user__username=self.request.user.username,
            is_complete=False
        )


class UserRegisterView(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'listapp/registration.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_custom_context(title='Registration Page')
        return dict(list(context.items()) + list(data.items()))


class UserAddTaskView(DataMixin, CreateView):
    form_class = AddTaskForm
    template_name = 'listapp/add_task.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_custom_context(title='Add Task')
        return dict(list(context.items()) + list(data.items()))

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class LoginUserView(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'listapp/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_custom_context(title='Login Page')
        return dict(list(context.items()) + list(data.items()))

    def get_success_url(self):
        return reverse_lazy('index')
