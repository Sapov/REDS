from django.contrib import admin
from django.contrib.auth import views
from django.urls import path
# from .views import *
from . import views
app_name = 'users'

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),

    path('signup/', views.SignUp.as_view(), name='signup'),
    path('user/<pk>', views.CustomUserUpdateView.as_view(), name='update_user'),
]
