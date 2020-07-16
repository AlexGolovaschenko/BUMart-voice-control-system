from django.urls import path
from voice_control import views

app_name = 'voice'

urlpatterns = [
	path('', views.home, name='home'),
    path('command', views.post_command, name='post_command'),
]
