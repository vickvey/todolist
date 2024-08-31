from rest_framework import viewsets
from api import models
from api import serializers

class TaskViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing tasks.
    """
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer