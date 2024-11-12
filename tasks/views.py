from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Task
from .serializers import TaskSerializer, UserSerializer

from django.utils.dateparse import parse_date
from .permissions import IsAdminOrOwner


class UserView(APIView):
    """
    View to handle user registration.
    """

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        """
        Registers a new user.
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskViewSet(ModelViewSet):
    """
    A viewset for managing tasks.

    Query parameters:
    - completed: filter by completion status (true or false).
    - created_after: filter tasks created after a specific date.
    - updated_after: filter tasks updated after a specific date.
    """

    serializer_class = TaskSerializer
    permission_classes = [IsAdminOrOwner]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        """
        Retrieves tasks based on user permissions.
        Admin users can view all tasks, while regular users only see their
        tasks.
        Filters by completion status, creation date, and update date if query
        parameters are provided.
        """
        if self.request.user.is_staff:
            queryset = Task.objects.select_related("user").all()
        else:
            queryset = Task.objects.select_related("user").filter(
                user=self.request.user
            )

        completed = self.request.query_params.get("completed")
        created_after = self.request.query_params.get("created_after")
        updated_after = self.request.query_params.get("updated_after")

        if completed is not None:
            queryset = queryset.filter(completed=completed.lower() == "true")

        if created_after:
            queryset = queryset.filter(
                created_at__date__gte=parse_date(created_after)
            )

        if updated_after:
            queryset = queryset.filter(
                updated_at__date__gte=parse_date(updated_after)
            )

        return queryset

    def perform_create(self, serializer):
        """
        Assigns the logged-in user as the owner of the task upon creation.
        """
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        """
        Ensures only the task owner can update the task.
        Raises PermissionDenied if the user is not the owner.
        """
        if serializer.instance.user != self.request.user:
            raise PermissionDenied(
                "You do not have permission to edit this task."
            )
        serializer.save()

    def perform_destroy(self, instance):
        """
        Ensures only the task owner can delete the task.
        Raises PermissionDenied if the user is not the owner.
        """
        if instance.user != self.request.user:
            raise PermissionDenied(
                "You do not have permission to delete this task."
            )
        instance.delete()
