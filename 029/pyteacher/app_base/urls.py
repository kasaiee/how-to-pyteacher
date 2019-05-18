"""pyteacher URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app_base import views

urlpatterns = [
    path('', views.home, name='home'),
    path('course-detail/<int:id>/', views.course_detail, name='course-detail'),
    path('courses-<int:course_id>/session-<int:session_id>/', views.course_session_detail, name='course-session-detail'),
    path('courses-<int:course_id>/session-<int:session_id>/exercise-<int:exercise_id>/', views.course_session_exercise_detail, name='course-session-exercise-detail'),
    path('register-course/<int:course_id>/', views.register_course, name='register-course'),
]
