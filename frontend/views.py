import requests
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.shortcuts import redirect
from .forms import TaskForm

API_BASE_URL = 'http://localhost:8000/api/taskapi/'

class TaskListView(ListView):
    template_name = 'frontend/task_list.html'

    def get_queryset(self):
        try:
            response = requests.get(API_BASE_URL)
            response.raise_for_status()
            tasks = response.json()
        except requests.RequestException as e:
            print(f'Error fetching tasks: {e}')
            tasks = []
        return tasks

class TaskCreateView(CreateView):
    form_class = TaskForm
    template_name = 'frontend/task_form.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        try:
            response = requests.post(API_BASE_URL, data=form.cleaned_data)
            response.raise_for_status()
        except requests.RequestException as e:
            form.add_error(None, f'Error creating task: {e}')
            return self.form_invalid(form)
        return super().form_valid(form)

class TaskUpdateView(UpdateView):
    form_class = TaskForm
    template_name = 'frontend/task_form.html'
    success_url = reverse_lazy('task_list')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        try:
            response = requests.get(f'{API_BASE_URL}/{pk}/')
            response.raise_for_status()
            task = response.json()
        except requests.RequestException as e:
            return redirect('task_list')
        return task

    def form_valid(self, form):
        pk = self.kwargs.get('pk')
        try:
            response = requests.put(f'{API_BASE_URL}/{pk}/', data=form.cleaned_data)
            response.raise_for_status()
        except requests.RequestException as e:
            form.add_error(None, f'Error updating task: {e}')
            return self.form_invalid(form)
        return super().form_valid(form)

class TaskDetailView(DetailView):
    template_name = 'frontend/task_detail.html'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        try:
            response = requests.get(f'{API_BASE_URL}/{pk}/')
            response.raise_for_status()
            task = response.json()
        except requests.RequestException as e:
            return redirect('task_list')
        return task
