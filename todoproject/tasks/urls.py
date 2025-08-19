from django.urls import path, include
from .views import task_list, task_create, task_toggle, task_delete , kanban_board ,update_task_status , dashboard
from rest_framework.routers import DefaultRouter
from .api_views import TaskViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r"tasks", TaskViewSet, basename="task")
router.register(r"categories", CategoryViewSet, basename="category")

urlpatterns = [
    path("", task_list, name="task_list"),
    path("create/", task_create, name="task_create"),
    path("toggle/<int:pk>/", task_toggle, name="task_toggle"),
    path("delete/<int:pk>/", task_delete, name="task_delete"),
    path("dashboard/", dashboard, name="dashboard"),
    path('kanban/', kanban_board, name='kanban_board'),
    path('update-status/',update_task_status, name='update_task_status'),
    path("api/", include(router.urls)),
]
