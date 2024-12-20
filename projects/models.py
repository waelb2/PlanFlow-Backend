from django.conf import settings
from django.db import models


class Project(models.Model):
    # Enums
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"

    PRIORITY_CHOICES = [
        (HIGH, "High"),
        (MEDIUM, "Medium"),
        (LOW, "Low"),
    ]

    NOT_STARTED = "Not Started"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"

    STATUS_CHOICES = [
        (NOT_STARTED, "Not Started"),
        (IN_PROGRESS, "In Progress"),
        (COMPLETED, "Completed"),
    ]

    # Fields
    title = models.CharField(max_length=72)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default=MEDIUM)
    category = models.CharField(max_length=32)
    status = models.CharField(
        max_length=15, choices=STATUS_CHOICES, default=NOT_STARTED
    )
    image_urls = models.JSONField(default=list, blank=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="projects"
    )

    # Keeping the tracking of creation
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
