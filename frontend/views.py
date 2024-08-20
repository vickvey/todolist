# frontend/views.py

import requests
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

API_URL = 'http://localhost:8000/api/taskapi/'

def task_list(request):
    response = requests.get(API_URL)
    tasks = response.json()
    return render(request, 'frontend/task_list.html', {'tasks': tasks})

def task_detail(request, id):
    response = requests.get(f"{API_URL}{id}/")
    task = response.json()
    return render(request, 'frontend/task_detail.html', {'task': task})

def task_create(request):
    if request.method == 'POST':
        data = {
            'title': request.POST['title'],
            'description': request.POST['description'],
        }
        response = requests.post(API_URL, data=data)
        return redirect('task_list')
    return render(request, 'frontend/task_form.html', {'action': 'Create'})

def task_update(request, id):
    task = get_object_or_404(requests.get(f"{API_URL}{id}/").json())
    if request.method == 'POST':
        data = {
            'title': request.POST['title'],
            'description': request.POST['description'],
        }
        response = requests.put(f"{API_URL}{id}/", data=data)
        return redirect('task_list')
    return render(request, 'frontend/task_form.html', {'task': task, 'action': 'Update'})

def task_delete(request, id):
    if request.method == 'POST':
        response = requests.delete(f"{API_URL}{id}/")
        return redirect('task_list')
    task = get_object_or_404(requests.get(f"{API_URL}{id}/").json())
    return render(request, 'frontend/task_confirm_delete.html', {'task': task})
