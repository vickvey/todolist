from core_api import models
from core_api import serializers
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response


def print_terminal_review(self, operation):
    print('*********' + operation + '*********')
    print('Basename: ', self.basename)
    print('Action: ', self.action)
    print('Detail: ', self.detail)
    print('Suffix: ', self.suffix)
    print('Name: ', self.name)
    print('Description: ', self.description)

class TaskViewSet(viewsets.ViewSet):
    def list(self, request):
        print_terminal_review(self, 'List')
        
        tasks=models.Task.objects.all()
        serializer=serializers.TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        print_terminal_review(self, 'Retrieve')
        if pk is not None:
            task=models.Task.objects.get(pk=pk)
            serializer=serializers.TaskSerializer(task)
            return Response(serializer.data)
        
    def create(self, request):
        print_terminal_review(self, 'Create')
        serializer=serializers.TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk):
        print_terminal_review(self, 'Update')
        task=models.Task.objects.get(pk=pk)
        serializer=serializers.TaskSerializer(task, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        print_terminal_review(self, 'Partial Update')
        task=models.Task.objects.get(pk=pk)
        serializer=serializers.TaskSerializer(task, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'})
        return Response(serializer.errors)
    
    def destroy(self, request, pk):
        print_terminal_review(self, 'Delete')
        task=models.Task.objects.get(pk=pk)
        task.delete()
        return Response({'msg': 'Data Deleted'})


