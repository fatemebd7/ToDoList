from django.urls import path, include
from tasks.views import task_list, task_create, task_toggle, task_delete, dashboard
from rest_framework.routers import DefaultRouter
from tasks.api_views import TaskViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r"tasks", TaskViewSet, basename="task")
router.register(r"categories", CategoryViewSet, basename="category")

urlpatterns = [
    path("", task_list, name="task_list"),
    path("create/", task_create, name="task_create"),
    path("toggle/<int:pk>/", task_toggle, name="task_toggle"),
    path("delete/<int:pk>/", task_delete, name="task_delete"),
    path("dashboard/", dashboard, name="dashboard"),
    path("api/", include(router.urls)),
]
