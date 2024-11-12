from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Task


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for creating and managing users.
    """

    class Meta:
        model = User
        fields = ["id", "username", "password", "email"]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        """
        Creates a new user with hashed password and saves them to the database.
        """
        user = User(
            username=validated_data["username"],
            email=validated_data["email"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for creating, updating, and retrieving task details.
    """

    class Meta:
        model = Task
        fields = [
            "id", "title", "description", "completed", "created_at",
            "updated_at"
        ]
        read_only_fields = ["created_at", "updated_at"]
