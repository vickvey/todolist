from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

# Creating Router Object
router=DefaultRouter()

# Register TaskViewSet with Router
router.register(r'tasks', views.TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)), # RESTful routes
]


