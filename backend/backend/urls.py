from django.contrib import admin
from django.urls import path, include
from api.views import CreateUserView
# These are pre-built views to obtain and refresh the jwt tokens.
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path("admin/", admin.site.urls),
    # as_view() essentially transforms a class-based view into a callable view function 
    # that can be used in your URL configurations.
    path("api/user/register/", CreateUserView.as_view(), name="register"),
    path("api/token/", TokenObtainPairView.as_view(), name="get_token"),
    path("api/token/refresh", TokenRefreshView.as_view(), name="refresh"),
    # Adds a set of default authentication-related URLs to your Django project, 
    # Provides endpoints for login, logout, and potentially other authentication tasks.
    # By including these URLs, you make it easier to manage user authentication in your
    # Django REST framework-powered API.
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include("api.urls")),              
]
