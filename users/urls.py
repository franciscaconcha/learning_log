"""Defines URL patterns for users."""
from django.urls import re_path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = 'users'

urlpatterns = [
	# Login page
	re_path(r'^login/$',
	        LoginView.as_view(template_name='users/login.html'),
	        name='login'),

	# Logout page
	re_path(r'^logout/$',
	        LogoutView.as_view(),
	        name='logout'),

	# Registration page
	re_path(r'^register/$', views.register, name='register')
]