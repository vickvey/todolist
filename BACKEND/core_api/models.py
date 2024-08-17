from django.db import models

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=100, unique=True)
    description=models.TextField()
    completed=models.BooleanField()
    
    # Add more attributes
    def __str__(self):
        return self.title