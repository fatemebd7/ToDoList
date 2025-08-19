from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from accounts.api_views import UserRegisterView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("tasks.urls")),
    path("accounts/", include("accounts.urls")), 
    path("api/auth/register/", UserRegisterView.as_view(), name="api_register"),
    path("api/auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
