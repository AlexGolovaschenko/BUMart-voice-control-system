from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
    path('command', views.post_command, name='post_command'),
]
