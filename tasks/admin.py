from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "id",
        "title",
        "description",
        "completed",
        "created_at",
        "updated_at",
    ]
