from . import views
from django.urls import path


urlpatterns = [
    path('test/', views.Test, name='test'),
    path('users/', views.Users, name='users')
]
