from django.urls import path
from .views import *

urlpatterns = [
    path("", apiOverview, name='api-overview' ),
    path("task-list/", taskList, name='task-list' ),
    path("task-detail/<str:pk>/", taskDetail, name='task-detail' ),
]
