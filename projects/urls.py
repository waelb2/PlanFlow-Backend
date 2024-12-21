from django.urls import path

from .views import (
    CreateProjectView,
    DeleteProjectView,
    UpdateProjectView,
    UserProjectsView,
)

urlpatterns = [
    path("", UserProjectsView.as_view(), name="get_projects"),
    path("create/", CreateProjectView.as_view(), name="create_project"),
    path("<int:pk>/", UpdateProjectView.as_view(), name="update_project"),
    path("<int:pk>", DeleteProjectView.as_view(), name="delete_project"),
]
