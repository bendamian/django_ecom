from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static
from product import views


# URL configuration for the Django project
urlpatterns = [
    # Admin panel route (e.g., http://localhost:8000/admin/)
    path('admin/', admin.site.urls),

    # Djoser provides RESTful authentication endpoints
    # Includes routes for user registration, password reset, etc.
    path('api/v1/', include('djoser.urls')),

    # Djoser token authentication endpoints (e.g., login, logout)
    path('api/v1/', include('djoser.urls.authtoken')),

    # Product app routes
    path('api/v1/', include('product.urls', namespace='product')),
]

# Serve media files (images, uploads, etc.) in development mode
# e.g., MEDIA_URL = '/media/' will make media accessible at http://localhost:8000/media/
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
