from django.contrib import admin
from django.urls import path, include
from core_api import views
from rest_framework.routers import DefaultRouter


# Creating Router Object
router=DefaultRouter()

# Register TaskViewSet with Router
router.register('taskapi', views.TaskViewSet, basename='task')

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('api/', include(router.urls)), # API routes under /api/
]
