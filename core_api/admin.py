from django.contrib import admin
from core_api import models

# Register your models here
admin.site.register([
    models.Task
])