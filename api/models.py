from django.db import models

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=100, unique=True)
    description=models.TextField(blank=True, null=True)
    completed=models.BooleanField(default=False)
    
    # Add more attributes
    def __str__(self):
        return str(self.title)