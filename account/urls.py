from django.urls import path, include
from . import views  # Import views module from current directory
from django.contrib.auth import views as auth_views  # Import views module from Django's contrib.auth package with an alias

# Define URL patterns
urlpatterns = [
    path("", include("django.contrib.auth.urls")),  # Include default authentication URLs provided by Django
    path("dashboard/", views.dashboard, name="dashboard"),  # Map dashboard view to /dashboard/ URL
    path("register/", views.register, name="register"),  # Map register view to /register/ URL
    path("edit/", views.edit, name="edit"),  # Map edit view to /edit/ URL
]
