from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tasks', TaskApiListViewSet, basename='task')
router.register(r'user', UserAPIListViewSet, basename='user')

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),

    
    path('task-list/', TaskAPIList.as_view(), name='task-list-create'),
    path('task-list/<int:pk>/', TaskAPIDetailView.as_view(), name='task-detail'),
    path('user-list/', UserAPIList.as_view(), name='user-list-create'),
    path('user-list/<int:pk>/', UserAPIDetailView.as_view(), name='user-detail'),
    path('api/query-task/', QueryTaskAPIView.as_view(), name='query-task'),
    path('api/', include(router.urls)),
]
