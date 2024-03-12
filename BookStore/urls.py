from django.contrib import admin  # Importing Django's admin module
from django.urls import path, include  # Importing functions for defining URL patterns
from django.conf import settings  # Importing Django's settings module
from django.conf.urls.static import static  # Importing static helper function

urlpatterns = [
    path("admin/", admin.site.urls),  # URL pattern for accessing the admin site
    path("account/", include("account.urls")),  # URL pattern for including account-related URLs
    path("", include("MainPage.urls")),  # URL pattern for including URLs from the MainPage app
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Adding URL patterns for serving media files during development
