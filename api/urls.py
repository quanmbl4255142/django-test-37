from django.urls import path
from . import views

urlpatterns = [
    path('userget/', views.UserListCreateView.as_view(), name='userget-list'),
    path('userget/<int:pk>/', views.UserDetailView.as_view(), name='userget-detail'),
    path('health/', views.health_check, name='health-check'),
]
