"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from base.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
    path('api/v1/tasklist', TaskAPIList.as_view()),
    path('api/v1/tasklist/<int:pk>/', TaskAPIUpdate.as_view()),
    path('api/v1/taskdetail/<int:pk>/', TaskAPIDetailView.as_view()),
    path('api/v1/userlist', UserAPIList.as_view()),
    path('api/v1/userlist/<int:pk>/', UserAPIUpdate.as_view()),
    path('api/v1/userdetail/<int:pk>/', UserAPIDetailView.as_view())
]
