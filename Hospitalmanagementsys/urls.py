from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from hospitalapp import views

urlpatterns = [
                  path('', include('hospitalapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
