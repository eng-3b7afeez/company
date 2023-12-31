from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import endpoints

urlpatterns = [
    path("", endpoints, name="endpoints"),
    path("users/", include("core.urls")),
    path("auth/", include("rest_framework.urls")),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("customers/", include("customers.urls")),
    path("operations/", include("operations.urls")),
]
