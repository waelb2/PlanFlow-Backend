from django.urls import path

from .views import CreateProjectView

urlpatterns = [
    path("", CreateProjectView.as_view(), name="create_project"),
    #    path("projects/update/<int:pk>/", UpdateProjectView.as_view(), name="update_project"),
    #    path("projects/delete/<int:pk>/", DeleteProjectView.as_view(), name="delete_project"),
]
