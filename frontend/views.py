import requests
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
import json

API_URL = 'http://localhost:8000/api/taskapi/'

def handle_api_request(method, url, data=None):
    try:
        if method == 'GET':
            response = requests.get(url)
        elif method == 'POST':
            response = requests.post(url, json=data)
        elif method == 'PUT':
            response = requests.put(url, json=data)
        elif method == 'DELETE':
            response = requests.delete(url)
        else:
            raise ValueError("Invalid method specified")
        
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        messages.error(method, f"An error occurred: {e}")
        return None

def task_list(request):
    tasks = handle_api_request('GET', API_URL)
    if tasks is None:
        return HttpResponse(status=500)  # Internal Server Error
    return render(request, 'frontend/task_list.html', {'tasks': tasks})

def task_detail(request, id):
    task = handle_api_request('GET', f"{API_URL}{id}/")
    if task is None:
        return HttpResponse(status=404)  # Not Found
    return render(request, 'frontend/task_detail.html', {'task': task})

def task_create(request):
    if request.method == 'POST':
        data = {
            'title': request.POST.get('title', ''),
            'description': request.POST.get('description', ''),
        }
        response = handle_api_request('POST', API_URL, data=data)
        if response is not None:
            messages.success(request, "Task created successfully!")
            return redirect('task_list')
        return HttpResponse(status=500)
    return render(request, 'frontend/task_form.html', {'action': 'Create'})

def task_update(request, id):
    task = handle_api_request('GET', f"{API_URL}{id}/")
    if task is None:
        return HttpResponse(status=404)  # Not Found
    
    if request.method == 'POST':
        data = {
            'title': request.POST.get('title', ''),
            'description': request.POST.get('description', ''),
        }
        response = handle_api_request('PUT', f"{API_URL}{id}/", data=data)
        if response is not None:
            messages.success(request, "Task updated successfully!")
            return redirect('task_list')
        return HttpResponse(status=500)
    
    return render(request, 'frontend/task_form.html', {'task': task, 'action': 'Update'})

def task_delete(request, id):
    task = handle_api_request('GET', f"{API_URL}{id}/")
    if task is None:
        return HttpResponse(status=404)  # Not Found
    
    if request.method == 'POST':
        response = handle_api_request('DELETE', f"{API_URL}{id}/")
        if response is not None:
            messages.success(request, "Task deleted successfully!")
            return redirect('task_list')
        return HttpResponse(status=500)
    
    return render(request, 'frontend/task_confirm_delete.html', {'task': task})
