import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

API_URL = 'http://localhost:8000/api/taskapi/'

def handle_api_request(method, url, data=None):
    try:
        if method == 'POST':
            response = requests.post(url, json=data)
        elif method == 'GET':
            response = requests.get(url)
        elif method == 'PATCH':
            response = requests.patch(url, json=data)
        elif method == 'PUT':
            response = requests.put(url, json=data)
        elif method == 'DELETE':
            response = requests.delete(url)
        else:
            raise ValueError("Unsupported HTTP method")
        
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.HTTPError as e:
        # Log the error or handle it as needed
        raise e

def task_list(request):
    try:
        tasks = handle_api_request('GET', API_URL)
        if tasks is None:
            raise ValueError("No tasks found")
    except requests.exceptions.HTTPError:
        messages.error(request, "Failed to fetch tasks.")
        return HttpResponse(status=500)  # Internal Server Error
    except ValueError as e:
        messages.error(request, str(e))
        return HttpResponse(status=500)  # Internal Server Error
    return render(request, 'frontend/task_list.html', {'tasks': tasks})

def task_detail(request, id):
    try:
        task = handle_api_request('GET', f"{API_URL}{id}/")
        if task is None:
            raise ValueError("Task not found")
    except requests.exceptions.HTTPError:
        messages.error(request, "Task not found.")
        return HttpResponse(status=404)  # Not Found
    except ValueError as e:
        messages.error(request, str(e))
        return HttpResponse(status=404)  # Not Found
    return render(request, 'frontend/task_detail.html', {'task': task})

def task_create(request):
    if request.method == 'POST':
        data = {
            'title': request.POST.get('title', ''),
            'description': request.POST.get('description', ''),
            'completed': 'false'
        }
        response = handle_api_request('POST', API_URL, data=data)
        if response is not None:
            messages.success(request, "Task created successfully!")
            return redirect('task_list')
        return HttpResponse(status=500)
    return render(request, 'frontend/task_form.html', {'action': 'Create'})

def task_update(request, id):
    try:
        task = handle_api_request('GET', f"{API_URL}{id}/")
        if task is None:
            raise ValueError("Task not found")
    except requests.exceptions.HTTPError:
        messages.error(request, "Task not found.")
        return HttpResponse(status=404)  # Not Found
    except ValueError as e:
        messages.error(request, str(e))
        return HttpResponse(status=404)  # Not Found

    if request.method == 'POST':
        data = {
            'title': request.POST.get('title', ''),
            'description': request.POST.get('description', ''),
            'completed': 'false'
        }
        try:
            response = handle_api_request('PUT', f"{API_URL}{id}/", data=data)
            messages.success(request, "Task updated successfully!")
            return redirect('task_list')
        except requests.exceptions.HTTPError as e:
            messages.error(request, f"Error updating task: {e}")
            return render(request, 'frontend/task_form.html', {'task': task, 'action': 'Update'})
    
    return render(request, 'frontend/task_form.html', {'task': task, 'action': 'Update'})

def task_delete(request, id):
    try:
        task = handle_api_request('GET', f"{API_URL}{id}/")
        if task is None:
            raise ValueError("Task not found")
    except requests.exceptions.HTTPError:
        messages.error(request, "Task not found.")
        return HttpResponse(status=404)  # Not Found
    except ValueError as e:
        messages.error(request, str(e))
        return HttpResponse(status=404)  # Not Found

    if request.method == 'POST':
        try:
            handle_api_request('DELETE', f"{API_URL}{id}/")
            messages.success(request, "Task deleted successfully!")
            return redirect('task_list')
        except requests.exceptions.HTTPError as e:
            messages.error(request, f"Error deleting task: {e}")
            return redirect('task_list')
    
    return render(request, 'frontend/task_confirm_delete.html', {'task': task})
