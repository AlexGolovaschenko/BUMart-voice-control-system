
from django.contrib import admin
from django.urls import path, include
import voice_control

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('voice_control.urls')),
]
