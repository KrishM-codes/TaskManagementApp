from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    """
    Model representing a task assigned to a user, with title, description,
    completion status, and timestamps for creation and last update.
    """

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="tasks"
    )

    def __str__(self):
        return self.title
