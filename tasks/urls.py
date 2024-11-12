from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import UserView, TaskViewSet
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r"tasks", TaskViewSet, basename="task")

urlpatterns = [
    path("register/", UserView.as_view(), name="register"),
    path(
        "api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path(
        "api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),
    path(
        "api/token/verify/", TokenVerifyView.as_view(), name="token_verify"
    ),
    path("api/", include(router.urls)),  # Includes TaskViewSet routes
]


if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
