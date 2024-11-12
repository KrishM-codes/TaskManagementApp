from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied


def custom_exception_handler(exc, context):
    """
    Custom exception handler to standardize error responses.
    """
    response = exception_handler(exc, context)

    if response is not None:
        if isinstance(exc, PermissionDenied):
            response.data["detail"] = (
                "You do not have permission to perform this action."
            )
        elif response.status_code == 404:
            response.data["detail"] = "The resource was not found."
        elif response.status_code == 400:
            response.data["detail"] = "Bad request. Check the request data."

    return response or Response(
        {"detail": "An error occurred."},
        status=(status.HTTP_500_INTERNAL_SERVER_ERROR)
        )
